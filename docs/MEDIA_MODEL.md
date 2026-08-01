# 台產報完整圖片資料架構

版本：V2.8 Complete Media Architecture  
更新日期：2026-08-01

## 目的

每一筆產品可分別保存：

- `media.main`：產品卡片與主要詳情圖。
- `media.gallery`：其他角度、包裝、情境與外觀圖片。
- `media.evidence`：型號、產地、製造商、標章、成分或其他查證照片。

圖片顯示與產品發布狀態完全分離。加入圖片、收藏或排序，均不得讓資料自動進入正式發布。

## 資料範例

```json
{
  "media": {
    "main": {
      "kind": "image",
      "url": "assets/images/products/example-main.webp",
      "alt": "產品正面主圖",
      "caption": "產品正面",
      "source_url": "https://example.com/product",
      "source_name": "品牌官方產品頁",
      "source_type": "official_product_page",
      "rights_status": "permission_pending",
      "checked_at": "2026-08-01"
    },
    "gallery": [],
    "evidence": []
  }
}
```

## `kind`

- `image`：實際圖片，必須有 `url`、`alt`、`source_name`、`rights_status`、`checked_at`。
- `placeholder`：尚無圖片時的圖示，必須有 `emoji` 與 `alt`。

## 權利狀態

- `permission_pending`：尚未確認可否使用。
- `permission_granted`：已取得使用許可。
- `owned`：自行拍攝或自有素材。
- `public_domain`：公有領域。
- `creative_commons`：依相應授權使用。
- `unknown`：來源或權利尚不明。
- `not_applicable`：圖示或非圖片素材。

## 前台規則

1. 卡片只使用 `media.main`。
2. Drawer 可切換主圖、圖片集與查證照片。
3. 圖片失敗時顯示產品 emoji fallback。
4. 外部 URL 只接受 HTTP／HTTPS。
5. JSON 中不允許用 `<img>` HTML 塞進 `emoji`。
6. 查證照片不得與一般情境圖混用。
7. `permission_pending` 圖片不得被視為已取得授權。
8. 圖片資料不能改變 `verification_status` 或 `publication_status`。
