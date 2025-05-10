# Hi there! It is Shinkaigyotti with Docker!

### Shinkaigyotti backend link: [backend repo link](https://github.com/aoiorio/Shinkaigyotti)
### Shinkaigyotti frontend link: [frontend repo link](https://github.com/aoiorio/Shinkaigyotti-front)

## About Shinkaigyotti
### Shinkaigyotti 〜あなたは深海魚だ〜

### 🐠 Shinkaigyotti???
- Shinkaigyottiは誰かを深海魚にすることができるWebアプリです。
- あなたの写真を認識して、一番一致する深海魚を表示します。
- 人間の姿をしていてもバレていますよ。

### 🧑🏼‍🌾 Images???
<img width="1440" alt="Screenshot 2025-02-04 at 21 33 22" src="https://github.com/user-attachments/assets/e51ac8b3-04fb-454c-b9a4-49b764aa5792" />
<img width="1440" alt="Screenshot 2025-02-04 at 21 41 49" src="https://github.com/user-attachments/assets/3d8e001e-31db-462a-974f-9ec33add6f64" />
<img width="1440" alt="Screenshot 2025-02-04 at 21 36 13" src="https://github.com/user-attachments/assets/e2ad6814-030e-45a8-b400-5aad2b89bb60" />

### ✋🏼 Commands for the future

- イメージに名前をつけてbuildができる
```
docker build . -t kdg-nginx
```

- imageの一覧を確認する
```
docker image ls
```

- 指定したimageを実行
```
docker run -it kdg-nginx
```


### 📜 Credits
- [How to create billing alarms with Terraform?](https://qiita.com/ngyuki/items/bbabe8252203634b6f47)
- [What is Terraform state?](https://zenn.dev/spacemarket/articles/b7bd1422b896ca)
- [What is terraform init command?](https://zenn.dev/ishii1648/articles/e3464a668978cb)

### 🏮 Error Solutions

- 1️⃣

```
Error: Failed to load plugin schemas
│
│ Error while loading schemas for plugin components: Failed to obtain provider schema: Could not load the schema for provider
│ registry.terraform.io/hashicorp/aws: failed to instantiate provider "registry.terraform.io/hashicorp/aws" to obtain schema: Unrecognized
│ remote plugin message:
│
│ This usually means that the plugin is either invalid or simply
│ needs to be recompiled to support the latest protocol...
```
- [Solve by restarting the Mac itself (Zenn)](https://zenn.dev/bun913/articles/m1-mac-terraform-unstable)
- [Solve by adding environment variable (Terraform Gives errors Failed to load plugin schemas, Stackoverflow)](https://stackoverflow.com/questions/70407525/terraform-gives-errors-failed-to-load-plugin-schemas)