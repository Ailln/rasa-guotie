# Rasa Guotie

🤖️🐱 一个基于 Rasa 的中文聊天机器人——`锅贴`。

> 众所（不）周知，「锅贴」是是我家的一只猫，我平时和他对话，他每次都回复我「喵」～而这个基于 Rasa 的聊天机器人就不一样了，他可以通过文字表达自己的想法，不信你试试！

## 快速上手

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

## Rasa 使用的常见问题

### 1 jieba + bert 结合使用出现错误

- 这是一个高频问题，具体的讨论见 [rasa issue](https://github.com/RasaHQ/rasa/issues/8381);
- 目前来看无法使用，建议使用自定义的 bert token 去完成分词，代码见 [bert_tokenizer](./components/bert_tokenizer.py)，配置见 [config](config.yml)。

## 许可证

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)

## 参考

- [Rasa docs](https://rasa.com/docs/)
- [rasa_ch_faq](https://github.com/Dustyposa/rasa_ch_faq)
- [chatbot](https://github.com/Ailln/chatbot)
