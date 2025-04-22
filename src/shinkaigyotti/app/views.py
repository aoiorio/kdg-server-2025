import imgsim
import numpy as np
import cv2
import requests

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from PIL import Image
from bs4 import BeautifulSoup

from .models import Post, ImageModel
from .serializers import PostSerializer, ImageSerializer

# 0. イメージを読み込む
# 1. スクレイピングする
# 2. distanceを比べる
# 3. 一番distanceが低い画像のurlを返す


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    serializer_class = PostSerializer

    filter_fields = "photo"


def load_image_from_url(url):
    # URLから画像をダウンロード
    response = requests.get(url)

    # レスポンスが成功かどうかチェック
    if response.status_code != 200:
        raise Exception(
            f"Failed to download image. Status code: {response.status_code}"
        )

    # 画像データをNumPy配列に変換
    image_array = np.frombuffer(response.content, np.uint8)

    # NumPy配列をOpenCV形式の画像にデコード
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    return image


# ベクトルに変換して写真の誤差の距離(distance)を返す (どれだけ画像が合っているか)
def find_matched_fish(fish_image, base_image):
    base_image = Image.open(base_image)
    base_image = base_image.convert("RGB")
    base_image = np.array(base_image)

    vtr = imgsim.Vectorizer()
    fish_vec = vtr.vectorize(fish_image)
    base_vec = vtr.vectorize(base_image)
    dist = imgsim.distance(fish_vec, base_vec)

    return dist


# スクレピングをして深海魚たちの画像をリストで返す
def get_fish_img_urls():
    img_urls = []
    page_url = "https://churaumi.okinawa/fishbook/area:%e6%b7%b1%e6%b5%b7%e3%81%b8%e3%81%ae%e6%97%85%20%e5%80%8b%e6%b0%b4%e6%a7%bd/"

    res = requests.get(page_url)
    soup = BeautifulSoup(res.text)

    img_tags = soup.find_all("img")

    # 特定のurlから始まるsrcしかとらない
    for img_tag in img_tags:
        img_url: str = img_tag.get("src")
        if img_url is not None and img_url.startswith(
            "/userfiles/fish_images/shinkaigyo"
        ):
            img_urls.append("https://churaumi.okinawa" + img_url)

    return img_urls


# 画像をpickするView
class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer  # check ユーザのどんなクエリを受け付けるか

    @action(detail=False, methods=["post"])
    def get_matched_fish(self, request):
        serializer = self.serializer_class(data=request.data)
        # もし画像ではないファイルが送られたらexceptionを出す
        serializer.is_valid(raise_exception=True)

        # ユーザーが選択した画像を取得
        base_image = request.data["image"]
        least_dis = 30
        res = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWNgaUn2Aqf7nP0a6zMW-WA4MppqcHvlVeVw&s"

        # 深海魚たちを取得
        img_urls = get_fish_img_urls()

        # マッチする深海魚を探すどん
        for url in img_urls:
            # サイトから持ってきた画像をvecに変換できるようにデコードする
            fish_image = load_image_from_url(url)
            num = find_matched_fish(fish_image, base_image)
            if num < least_dis:
                res = url
                least_dis = num
        print(res)

        return Response({"matched_fish": res}, status=status.HTTP_200_OK)
