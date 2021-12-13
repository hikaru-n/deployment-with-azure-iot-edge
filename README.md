# deployment-with-azure-iot-edge

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

```shell-session_
$ az iot hub monitor-events --output table --hub-name $TF_VAR_iothub_name
```
