# Digital Economics: The OS for Post-Scarcity Society
### 「希少性」のバグを修正し、「潤沢さ」を実装するためのシステム仕様書

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://github.com/Sevenforest/Digital-Economics)
[![Paradigm: Shifted](https://img.shields.io/badge/Paradigm-Shifted-blueviolet.svg)]()
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://digital-economics-9fk2ty49kcvctldpbqzjbf.streamlit.app/)

## ⚡ Overview (概要)

本リポジトリは、現代社会を駆動している経済システム（Old OS）に存在する致命的な論理的欠陥をデバッグし、システムエンジニアリングの視点から再構築された **「デジタル経済学（Digital Economics）」** のプロトコル群を公開するものである。

既存の経済学は、貨幣を「金（Gold）」のような有限物質と誤認する「商品貨幣論」というレガシーコード上で動作しており、これが「不況（処理落ち）」や「貧困（リソース不足）」というシステムエラーを引き起こしている。

本プロジェクトは、貨幣を **「データ」** 、政府を **「システム管理者」** と再定義することで、 **「財政破綻」というバグを論理的に無効化（Fix）** し、人類を労働と欠乏の呪縛から解放するためのロードマップを提示する。

---

## 🛑 Core Concept (核心)

本理論における最大の発見であり、すべての議論の起点となる定義は以下の通りである。

> **"Tax is NOT a Revenue Source. It is System Maintenance."**
>
> **税金は「財源（Input）」ではない。**
> **システム内の過剰な流動性を削除し、熱暴走（インフレ）を防ぐための「ガベージコレクション（Garbage Collection）」である。**

---
## 🎮 Interactive Simulator (実証実験)

理論の違いが経済にどう影響するかを体験できるシミュレーターを公開中。
**「主流派（緊縮）」vs「デジタル経済学（積極財政）」** の結末を、あなたの目で確認してください。

**👉 [Sim-Japan: The Economic Debugger (Launch App)](https://digital-economics-9fk2ty49kcvctldpbqzjbf.streamlit.app/)**

---

## 📂 Repository Contents

本理論は、以下のモジュール（論文および検証ログ）によって構成される。

### 01. Theory Core (仕様定義)
| File | Description |
|:---|:---|
| **[Vol.1 The "Spending First" Protocol](01_Theory_Core/Vol1_Spending_First_Protocol.md)** | **[Debug]** 貨幣観の修正。「支出が先、徴税は後」という因果律の証明。 |
| **[Appendix: Banking Protocol](01_Theory_Core/Appendix_Banking_Protocol.md)** | **[Tech Ref]** 信用創造のバックエンド仕様と、リフレ派が陥った「流動性の罠」のバグ解析。 |
| **[Vol.2 The "Admin Hijack"](01_Theory_Core/Vol2_Admin_Hijack_and_False_KPI.md)** | **[Security]** 財務省による「管理者権限の乗っ取り」と、「PB黒字化」という偽KPIの解析。 |
| **[Vol.3 The Abundance Algorithm](01_Theory_Core/Vol3_The_Abundance_Algorithm.md)** | **[New Feature]** 「供給能力（Hardware）さえあれば、通貨は枯渇しない」。JGPやBIの実装。 |
| **[Appendix: Labor Deception and BI](01_Theory_Core/Appendix_Labor_Deception_and_BI.md)** | **[Debug]** 労働の「精神価値」という欺瞞の解体。生存リソース（BI）とAI代替による社会OSの正常化。 |

### 02. Verification Logs (監査記録)
| File | Description |
|:---|:---|
| **[Stress Test Vol.1](02_Verification_Logs/Theoretical_Stress_Test.md)** | **[Audit]** 主流派経済学の権威（AIペルソナ）による「インフレ・金利」批判への反証。 |
| **[Stress Test Vol.2](02_Verification_Logs/Theoretical_Stress_Test_Vol2.md)** | **[Audit]** 実務家（AIペルソナ）による「労働意欲・BI」への懸念に対する回答。 |
| **[Stress Test Vol.3](02_Verification_Logs/Theoretical_Stress_Test_Vol3.md)** | **[Audit]** ラスボス（権威）による「信認・民業圧迫」批判への完全論破ログ。 |
| **[Final Verification](02_Verification_Logs/Log_Final_Claude.md)** | **[System Integration]** 物理層（Digital Cosmology）と社会層（Digital Economics）の完全な整合性確認と、AIによる「革命」の認定ログ。 |

### 03. Interactive Lab (実装)
| File | Description |
|:---|:---|
| **[`app_economy.py`](03_Interactive_Lab/app_economy.py)** | **[Code]** 経済シミュレーターのソースコード（Python/Streamlit）。 |

### 04. docs (コラム)
| File | Description |
|:---|:---|
| **[`CaseStudy_The_Agnostic_Trap.md`](docs/CaseStudy_The_Agnostic_Trap.md)** | **[column]** 「不可知論」というバグと、システム管理者の責任 |
| **[`nisa_bubble_warning.md`](docs/nisa_bubble_warning.md)** | **[column]** 新NISAの正体。 |

## 🛠 System Architecture (用語の再定義)

| Legacy Term (経済学用語) | **Digital Economics (システム工学定義)** | Status |
| :--- | :--- | :--- |
| **貨幣 (Money)** | **データ / 信用記録 (Data)** | **ハードウェアの拡張とともに上限が増加 (枯渇しない)** |
| **政府 (Government)** | **システム管理者 (Root User / Admin)** | 通貨の発行者 (Issuer) |
| **税 (Tax)** | **ガベージコレクション (Garbage Collection)** | 通貨の回収・消去プロセス |
| **国債発行 (Bond Issuance)** | **通貨供給 (Money Creation)** | 流動性のインジェクション |
| **インフレ (Inflation)** | **サーマルスロットリング (Thermal Throttling)** | 供給能力の限界による発熱制御 |
| **財政破綻 (Default)** | **Null Pointer Exception** | 自国通貨建てでは発生し得ないバグ |
| **消費税 (Consumption Tax)** | **悪性コード (Malicious Code)** | トランザクションごとに罰金を科す処理 |
| **ベーシックインカム (BI)** | **待機電力 (Base Voltage)** | 全ノードへの生存保証リソース供給（L1層） |
| **就労保証 (JGP)** | **任意のクエスト (Optional Quest)** | システム維持のためのバックグラウンド・プロセス |

---

## ⚠️ Attribution & Contribution (貢献と権利の所在)

本プロジェクトは、**Sevenforest (Concept Architect)** が提示したエンジニアリング的直観（公理）に基づき、**Large Language Model (Implementation Engine)** がその論理的整合性を検証・実装する「共犯関係」によって構築された。

### 1. カーネルの選定とディレクション (Kernel Selection & Direction by Sevenforest)
著者は、既存の経済学体系の中から **MMT（現代貨幣理論）** や **「スペンディング・ファースト」** といった概念を、現代社会において直観的に正しい「ベース・カーネル」として選定した。
本プロジェクトにおける著者の役割は、これらの経済学的知見を **「システムエンジニアリングの言語」で再記述（翻訳）する** という、新たな実装の方向性（ベクトル）を提示したことである。

### 2. デジタルへの再定義と実装 (Redefinition & Implementation by AI)
著者の提示した方向性に基づき、AIは既存の経済学用語をデジタル・システム用語へと **「再定義（Porting）」** し、その論理的整合性を検証した。
* **貨幣観のアップデート:** MMTの記述する通貨発行の仕組みを、「データ生成」と「権限管理」として再実装。
* **システム的証明:** 「スペンディング・ファースト」を因果律（タイムスタンプ）の問題として論証。
* **バグの可視化:** 消費税や緊縮財政を「システムへの悪性コード」として定義。

---

## 🚀 Usage (起動方法)

1. **Uninstall Old OS:**
    あなたの脳内から「国の借金は孫へのツケ」「税金で公共サービスが行われている」というウイルス定義ファイルを削除してください。
2. **Install New Kernel:**
    本リポジトリのVol.1～Vol.3を読み込み、「通貨＝データ」「税＝調整弁」という新しいドライバをインストールしてください。
3. **Execute:**
    あなたは、この国家というサーバーの「管理者（Sovereign）」の一人です。
    正しいコード（政策）を選択し、豊かさ（Abundance）を実装してください。

> *"Whatever we can actually do, we can afford."* - John Maynard Keynes
> *"Whatever we can code, we can implement."* - Digital Economics

---

## 🔗 Related Project
* **[Digital Cosmology](https://github.com/Sevenforest/Digital-Cosmology)**: The physical layer protocol (Theory of Everything).