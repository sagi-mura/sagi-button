# 憨憨按钮 / Sagi 按钮 / Sagi Button

![https://www.bilibili.com/read/cv26475893/?spm_id_from=444.42.rich-text.link.click](https://github.com/sagi-mura/sagi-button/blob/master/public/img/sagi.jpg?raw=true)

### 网页地址

- [https://sagi.moe/](http://sagi.moe/)

### 相关链接：

- [星河Sagi 的 Bilibili 直播间](https://live.bilibili.com/30180399)

### 参与完善本项目

- 您可以在[Issues](https://github.com/sagi-mura/sagi-button/issues)提出您的建议。
- 请求添加新语音，请在[Sagi Button音频收集表](https://docs.qq.com/form/page/DR01DZWpLRHZOUVRI)提交你的音频
    - 我会不定期将收集表的音频更新到[https://sagi.moe/](http://sagi.moe/)上
    - 如果你发现收集表中的音频已经被添加到[https://sagi.moe/](http://sagi.moe/)上，那么请不要再次提交
    - 如果你发现收集表中的音频已经被添加到[https://sagi.moe/](http://sagi.moe/)上，但是你认为音频的质量不够好，请直接[Bilibili](https://space.bilibili.com/382322)私信我

### 添加或修改音频/完善翻译

音频文件推荐使用**mp3**格式，请先音量标准化，然后放入`public/voices/`目录

所有的分类和音频信息都存储在`setting/translate`目录的`json`文件中，**添加或修改音频信息**、**完善翻译**，你需要修改对应文件中的内容

`locales.json`和`category.json`分别为 UI 界面翻译和分类信息，请不要修改文件名，语音信息可以使用除此外的任意名称，可使用多个`json`文件方便管理语音

可使用`schema`文件夹中的`json`文件增加`json schema`约束和代码提醒

`category.json`结构示例如下：

```jsonc
[
  {
    "name": "名言",
    "translate": {
      "zh-CN": "憨憨名言~",
      "en-US": "Witticisms~"
    }
  },
  {
    "name": "星河",
    "translate": {
      "zh-CN": "星河~",
      "en-US": "Hoshikawa~"
    }
  }
]
```

语音文件结构示例如下：

```jsonc
[
  {
    "name": "青眼白龙",
    "path": "blue-eyes-white-dragon.mp3",
    "date": "2023-9-23",
    "translate": {
      "zh-CN": "青眼白龙",
      "en-US": "Blue eyes white dragon"
    },
    "usePicture": {
      "zh-CN": "dragon.jpg",
      "en-US": "dragon.jpg"
    },
    "category": "名言",
    "mark": {
      "title": "【唱歌杂谈】星河Sagi 2023年9月12日20点场",
      "time": "27:56~28:00",
      "url": "https://www.bilibili.com/video/BV1hz4y1573x"
    }
  },
  {
    "name": "多拉贡",
    "path": "dragon.mp3",
    "date": "2023-9-23",
    "translate": {
      "zh-CN": "多拉贡",
      "en-US": "Dragon"
    },
    "usePicture": {
      "zh-CN": "dragon.jpg",
      "en-US": "dragon.jpg"
    },
    "category": "名言",
    "mark": {
      "title": "【唱歌杂谈】星河Sagi 2023年9月12日20点场",
      "time": "28:00~28:04",
      "url": "https://www.bilibili.com/video/BV1hz4y1573x"
    }
  }
]
```

### LICENSE

- 使用[voices-button-cli](https://github.com/blacktunes/voices-button-cli)创建的语音按钮
- 所用模板为[Hiiro 按钮](https://github.com/blacktunes/hiiro-button)
