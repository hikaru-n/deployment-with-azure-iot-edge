# Azure IoT Edge を使用したモデルのデプロイ

(ドキュメント作成中です。)

このリポジトリは、[Azure IoT Edge](https://docs.microsoft.com/ja-jp/azure/iot-edge/about-iot-edge?view=iotedge-2020-11) を使用して Jetson にモデルをリモートでデプロイした際の作業記録です。

趣味の領域で簡単に試みたため、拙い箇所等ございますがご容赦ください。

実際に手を動かして試したい場合は[ドキュメント群](/docs)を参照してください。

以下に使用したデバイスとその用途を示します。

## 開発環境

CPU のアーキテクチャは AMD64 を使用しました。

OS や、 Docker のバージョンは以下を参照してください。

```shell-session
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.3 LTS
Release:        20.04
Codename:       focal

$ docker -v
Docker version 20.10.12, build e91ed57
```

## 実行環境

実行環境には Jetson Nano を採用しました。

OS や Docker のバージョンは以下を参照してください。

```shell-session
$ cat /etc/nv_tegra_release
# R32 (release), REVISION: 6.1, GCID: 27863751, BOARD: t210ref, EABI: aarch64, DATE: Mon Jul 26 19:20:30 UTC 2021

$ docker -v
Docker version 20.10.7, build 20.10.7-0ubuntu5~18.04.3

$ apt show nvidia-container-toolkit
Package: nvidia-container-toolkit
Version: 1.7.0-1
...
```

## 要求

Azure のサービスを使用するため、Azure のアカウントを所有していない場合はアカウントを取得してください。

## デバイスの登録

```shell-session
$ az extension add --upgrade --name azure-iot
```

```shell-session
$ az iot hub device-identity create --device-id edgeDevice --edge-enabled --hub-name $TF_VAR_iothub_name
```

```shell-session
$ az iot hub device-identity connection-string show --device-id edgeDevice --hub-name $TF_VAR_iothub_name
```

## IoTHub に送信されたメッセージを確認する

```shell-session
$ az iot hub monitor-events --output table --hub-name $TF_VAR_iothub_name
```

## Jetson に認証させる

リポジトリ構成パッケージをインストールする。

```shell-session
curl https://packages.microsoft.com/config/ubuntu/18.04/multiarch/packages-microsoft-prod.deb > ./packages-microsoft-prod.deb
```

構成パッケージのインストール

```shell-session
sudo apt install ./packages-microsoft-prod.deb
```

IoT エッジのランタイムのインストール

```shell-session
sudo apt-get update
sudo apt-get install iotedge
```

`/etc/iotedge/config.yml` を編集する

```shell-session
sudo systemctl restart iotedge
sudo systemctl daemon-reaload
```
