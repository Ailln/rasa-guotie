# Rasa Guotie

🤖️🐱 一个基于 Rasa 的中文聊天机器人——`锅贴`。

> 众所（不）周知，「锅贴」是是我家的一只猫，我平时和他对话，他每次都回复我「喵」～而这个基于 Rasa 的聊天机器人就不一样了，他可以通过文字表达自己的想法，不信你试试！

[![](.github/src/guotie_v0-1-0_test.png)](https://guotie.ailln.com/guest/conversations/production/12fd779ce02a45d495d85613beb3d676)

[🔗 Demo Link](https://guotie.ailln.com/guest/conversations/production/12fd779ce02a45d495d85613beb3d676)

## 1 快速上手

### 1.1 训练 Rasa Model

```bash
# 安装
pip install -r requirements.txt

# 训练
rasa train

# 在 shell 中与「锅贴」对话
rasa shell
# Bot loaded. Type a message and press enter (use '/stop' to exit): 
# Your input ->  你好                     
# 你好啊！我是锅贴，喵～
# Your input ->  你多大啦
# 喵龄 3 岁，嘿嘿！
# Your input ->  你爸爸是谁啊
# 我爸妈都是 Ailln，他是我的铲屎官。
# Your input ->  再见
# 再见呀！我会想你的，喵～

# 启动 API 服务
rasa run --enable-api
```

### 1.2 使用 Rasa X

```bash
# 安装
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple

# 运行 rasa x
rasa x

# 运行 action
rasa run actions --debug
```

## 2 Rasa 使用的常见问题

### 2.1 jieba + bert 结合使用出现错误

- 这是一个高频问题，具体的讨论见 [rasa issue](https://github.com/RasaHQ/rasa/issues/8381);
- 目前来看无法使用，建议使用自定义的 bert token 去完成分词，代码见 [bert_tokenizer](./components/bert_tokenizer.py)，配置见 [config](config.yml)。

### 2.2 安装 rasa x 超时

```bash
INFO: This is taking longer than usual. You might need to provide the dependency resolver with stricter constraints to \
reduce runtime. If you want to abort this run, you can press Ctrl + C to do so. To improve how pip performs, tell us \
what happened here: https://pip.pypa.io/surveys/backtracking
```

问题讨论见[论坛](https://forum.rasa.com/t/pip-is-taking-longer-than-usual/39263)，它是由 pip v20.3中引入的依赖性解析回溯逻辑引起的，解决方法是安装回 v20.2。

```bash
pip install pip==20.2
```

### 2.3 运行 rasa x 命令时出错

```bash
from socketio import AsyncServer
ImportError: cannot import name 'AsyncServer'
```

安装合适版本的 python-socketio 和 python-engineio。

参考配置：在 rasa x 为 0.39.3 时，python-socketio 为 5.0.0，python-engineio 为 3.13.0。

## 3 许可证

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)

## 4 参考

- [Rasa docs](https://rasa.com/docs/)
- [rasa_ch_faq](https://github.com/Dustyposa/rasa_ch_faq)
- [chatbot](https://github.com/Ailln/chatbot)
