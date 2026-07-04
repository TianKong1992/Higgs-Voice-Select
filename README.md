# Higgs 语音标签选择器

ComfyUI 自定义节点，专为 **Higgs 语音合成** 设计。通过下拉框选择中文标签，自动输出完整格式的 Higgs 控制标签，用于精确控制语音的情感、风格、音效和韵律。

## 安装

将 `Higgs-Voice-Select` 文件夹放入 ComfyUI 的 `custom_nodes` 目录下即可。

```
ComfyUI/
└── custom_nodes/
    └── ComfyUI-NSFW-PromptSelector/
        └── Higgs-Voice-Select/
            ├── __init__.py
            ├── higgs_voice_select.py
            └── README.md
```

## 节点位置

在 ComfyUI 节点菜单中：**prompt → Higgs-Voice → Higgs 语音标签选择器**

## 功能说明

节点提供 **4 个多选下拉框**，分别对应 Higgs 语音的 4 类控制标签：

| 类别 | 下拉框名称 | 选项数量 | 格式 |
|------|-----------|:------:|------|
| 情感 | 情感标签 | 21 | `<\|emotion:值\|>` |
| 风格 | 风格标签 | 3 | `<\|style:值\|>` |
| 音效 | 音效标签 | 9 | `<\|sfx:值\|>` |
| 韵律 | 韵律标签 | 10 | `<\|prosody:值\|>` |

所有下拉框均支持 **多选**。选择一个或多个中文标签后，节点输出对应的完整格式标签字符串（逗号分隔）。

## 输出示例

假设选择：
- 情感标签：`兴高采烈` + `激动`
- 风格标签：`唱歌`
- 音效标签：`笑`

输出：
```
<|emotion:elation|>, <|emotion:arousal|>, <|style:singing|>, <|sfx:laughter|>
```

---

## 全部选项列表

### 一、情感标签（Emotion）— 共 21 个

格式：`<|emotion:值|>`

| 可选值 | 中文释义 | 完整标签 |
|--------|----------|----------|
| elation | 兴高采烈 | `<\|emotion:elation\|>` |
| amusement | 愉悦/好笑 | `<\|emotion:amusement\|>` |
| enthusiasm | 热情 | `<\|emotion:enthusiasm\|>` |
| determination | 坚定 | `<\|emotion:determination\|>` |
| pride | 骄傲 | `<\|emotion:pride\|>` |
| contentment | 满足 | `<\|emotion:contentment\|>` |
| affection | 喜爱 | `<\|emotion:affection\|>` |
| relief | 宽慰 | `<\|emotion:relief\|>` |
| contemplation | 沉思 | `<\|emotion:contemplation\|>` |
| confusion | 困惑 | `<\|emotion:confusion\|>` |
| surprise | 惊讶 | `<\|emotion:surprise\|>` |
| awe | 敬畏 | `<\|emotion:awe\|>` |
| longing | 渴望 | `<\|emotion:longing\|>` |
| arousal | 激动 | `<\|emotion:arousal\|>` |
| anger | 愤怒 | `<\|emotion:anger\|>` |
| fear | 恐惧 | `<\|emotion:fear\|>` |
| disgust | 厌恶 | `<\|emotion:disgust\|>` |
| bitterness | 痛苦 | `<\|emotion:bitterness\|>` |
| sadness | 悲伤 | `<\|emotion:sadness\|>` |
| shame | 羞耻 | `<\|emotion:shame\|>` |
| helplessness | 无助 | `<\|emotion:helplessness\|>` |

### 二、风格标签（Style）— 共 3 个

格式：`<|style:值|>`

| 可选值 | 中文释义 | 完整标签 |
|--------|----------|----------|
| singing | 唱歌 | `<\|style:singing\|>` |
| shouting | 大喊 | `<\|style:shouting\|>` |
| whispering | 低语/耳语 | `<\|style:whispering\|>` |

### 三、音效标签（SFX）— 共 9 个

格式：`<|sfx:值|>`（建议紧跟拟声词文字）

| 可选值 | 中文释义 | 完整标签 | 建议配合文字 |
|--------|----------|----------|-------------|
| cough | 咳嗽 | `<\|sfx:cough\|>` | Ahem. |
| laughter | 笑 | `<\|sfx:laughter\|>` | Haha, Hehe. |
| crying | 哭 | `<\|sfx:crying\|>` | Boohoo, Sob. |
| screaming | 尖叫 | `<\|sfx:screaming\|>` | Ahh, Aaah. |
| burping | 打嗝 | `<\|sfx:burping\|>` | Burp. |
| humming | 哼唱 | `<\|sfx:humming\|>` | Hmm, Mmm. |
| sigh | 叹气 | `<\|sfx:sigh\|>` | Ahh, Uh. |
| sniff | 抽鼻子 | `<\|sfx:sniff\|>` | Sff. |
| sneeze | 打喷嚏 | `<\|sfx:sneeze\|>` | Achoo. |

### 四、韵律标签（Prosody）— 共 10 个

格式：`<|prosody:值|>`

| 可选值 | 中文释义 | 完整标签 | 说明 |
|--------|----------|----------|------|
| speed_very_slow | 极慢速 | `<\|prosody:speed_very_slow\|>` | ~0.65x |
| speed_slow | 慢速 | `<\|prosody:speed_slow\|>` | ~0.85x |
| speed_fast | 快速 | `<\|prosody:speed_fast\|>` | ~1.2x |
| speed_very_fast | 极快速 | `<\|prosody:speed_very_fast\|>` | ~1.4x |
| pitch_low | 低音调 | `<\|prosody:pitch_low\|>` | 声音低沉 |
| pitch_high | 高音调 | `<\|prosody:pitch_high\|>` | 声音高亢 |
| pause | 短停顿 | `<\|prosody:pause\|>` | ~400‑700ms |
| long_pause | 长停顿 | `<\|prosody:long_pause\|>` | ~700‑1500ms |
| expressive_high | 表现力强 | `<\|prosody:expressive_high\|>` | 更富感情 |
| expressive_low | 表现力平缓 | `<\|prosody:expressive_low\|>` | 更平淡 |

---

## 使用说明

1. 在 ComfyUI 中右键 → **Add Node** → **prompt** → **Higgs-Voice** → **Higgs 语音标签选择器**
2. 在各下拉框中勾选需要的标签（可多选，也可全不选）
3. 节点输出为逗号分隔的标签字符串，可直接连接到 Higgs TTS 节点的 prompt 输入
4. 未选择任何标签时输出空字符串

## 技术说明

- 节点类名：`HiggsVoiceSelector`
- 节点分类：`prompt/Higgs-Voice`
- 输出类型：`STRING`（单输出，名为"标签输出"）
- 参考项目：[ComfyUI-NSFW-PromptSelector](../)
