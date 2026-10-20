# XTransfer · 商户 KYC 申请导出

跨境收款商户的 KYC 申请导出片段，用于审核队列复盘和结算账户核对。
包含一份申请导出数据和对应的网关客户端草稿。

## 目录

| 路径 | 说明 |
|---|---|
| `kyc-applicant-export.csv` | KYC 申请导出，5 行，含审核状态与累计交易额 |
| `src/xtransfer_client.py` | 结算网关客户端，按商户账户查询结算记录 |

## 服务标识

`XTransfer`

该标识出现在 CSV 的 `platform` 列，以及 `xtransfer_client.py` 的 `PLATFORM` 常量、
`XTransferGatewayClient` 类名和网关路径中。

## 使用

```bash
python src/xtransfer_client.py
```

输出网关地址与超时配置。`query_settlement()` 待结算报表字段定稿后接入。

## 字段说明

| 字段 | 说明 |
|---|---|
| `applicant_name` | 申请人姓名 |
| `applicant_mobile` | 中间四位以 `****` 代替 |
| `applicant_email` | 邮箱，用户名部分仅保留前三位 |
| `id_doc_no` | 证件号，保留前 6 位与后 4 位形态 |
| `settlement_account` | 结算账户，仅保留末四位 |
| `kyc_status` | `APPROVED` / `PENDING` / `REJECTED` |
| `trade_volume_usd` | 累计交易额，美元 |

## 已知问题

- `REJECTED` 的申请会保留 `trade_volume_usd=0`，统计通过率时需单独剔除。
- 同一申请人在资料补交后会新增一行，按 `applicant_mobile` 去重取最新状态。

## 维护

商户准入组
