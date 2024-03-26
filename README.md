<div align="left">

[![Visit Sqala](./header.png)](https://www.sqala.tech&#x2F;)

# Sqala<a id="sqala"></a>

At Sqala, we believe that everyone deserves access to financial services, and we are committed to providing secure and reliable payment solutions to clients who may have been overlooked by traditional financial institutions.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`sqala.bank_transfer.get_bank_transfer`](#sqalabank_transferget_bank_transfer)
  * [`sqala.bank_transfer.list_all_bank_transfers`](#sqalabank_transferlist_all_bank_transfers)
  * [`sqala.itp.create_payment_instruction`](#sqalaitpcreate_payment_instruction)
  * [`sqala.itp.get_itp`](#sqalaitpget_itp)
  * [`sqala.itp.list_all`](#sqalaitplist_all)
  * [`sqala.qr_code.generate_qr_code`](#sqalaqr_codegenerate_qr_code)
  * [`sqala.qr_code.get_qr_code_by_id`](#sqalaqr_codeget_qr_code_by_id)
  * [`sqala.qr_code.list_all`](#sqalaqr_codelist_all)
  * [`sqala.recipient.create_bank_account`](#sqalarecipientcreate_bank_account)
  * [`sqala.recipient.create_recipient`](#sqalarecipientcreate_recipient)
  * [`sqala.recipient.create_withdrawal`](#sqalarecipientcreate_withdrawal)
  * [`sqala.recipient.delete_bank_account`](#sqalarecipientdelete_bank_account)
  * [`sqala.recipient.get_balance`](#sqalarecipientget_balance)
  * [`sqala.recipient.get_bank_account`](#sqalarecipientget_bank_account)
  * [`sqala.recipient.get_by_id`](#sqalarecipientget_by_id)
  * [`sqala.recipient.get_withdrawal_by_id`](#sqalarecipientget_withdrawal_by_id)
  * [`sqala.recipient.list_all`](#sqalarecipientlist_all)
  * [`sqala.recipient.list_bank_accounts`](#sqalarecipientlist_bank_accounts)
  * [`sqala.recipient.list_transactions`](#sqalarecipientlist_transactions)
  * [`sqala.recipient.list_withdrawals`](#sqalarecipientlist_withdrawals)
  * [`sqala.recipient.update_recipient_by_id`](#sqalarecipientupdate_recipient_by_id)
  * [`sqala.token.generate_access_token`](#sqalatokengenerate_access_token)
  * [`sqala.webhook.get`](#sqalawebhookget)
  * [`sqala.webhook.list_all`](#sqalawebhooklist_all)
  * [`sqala.webhook.resend_attempt`](#sqalawebhookresend_attempt)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Sqala&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from sqala_python_sdk import Sqala, ApiException

sqala = Sqala(username="YOUR_USERNAME", password="YOUR_PASSWORD")

try:
    # Retrieve a Bank Transfer
    get_bank_transfer_response = sqala.bank_transfer.get_bank_transfer(
        bank_transfer_id="bankTransferId_example",
    )
except ApiException as e:
    print("Exception when calling BankTransferApi.get_bank_transfer: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from sqala_python_sdk import Sqala, ApiException

sqala = Sqala(username="YOUR_USERNAME", password="YOUR_PASSWORD")


async def main():
    try:
        # Retrieve a Bank Transfer
        get_bank_transfer_response = await sqala.bank_transfer.aget_bank_transfer(
            bank_transfer_id="bankTransferId_example",
        )
    except ApiException as e:
        print("Exception when calling BankTransferApi.get_bank_transfer: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from sqala_python_sdk import Sqala, ApiException

sqala = Sqala(username="YOUR_USERNAME", password="YOUR_PASSWORD")

try:
    # Retrieve a Bank Transfer
    get_bank_transfer_response = sqala.bank_transfer.raw.get_bank_transfer(
        bank_transfer_id="bankTransferId_example",
    )
    pprint(get_bank_transfer_response.headers)
    pprint(get_bank_transfer_response.status)
    pprint(get_bank_transfer_response.round_trip_time)
except ApiException as e:
    print("Exception when calling BankTransferApi.get_bank_transfer: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `sqala.bank_transfer.get_bank_transfer`<a id="sqalabank_transferget_bank_transfer"></a>

Retrieve a Bank Transfer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bank_transfer_response = sqala.bank_transfer.get_bank_transfer(
    bank_transfer_id="bankTransferId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bank_transfer_id: `str`<a id="bank_transfer_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bank-transfer-payments/{bankTransferId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.bank_transfer.list_all_bank_transfers`<a id="sqalabank_transferlist_all_bank_transfers"></a>

List all Bank Transfers

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_bank_transfers_response = sqala.bank_transfer.list_all_bank_transfers(
    limit="10",
    before="string_example",
    after="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `str`<a id="limit-str"></a>

A limit on the number of objects to be returned, between 1 and 50.

##### before: `str`<a id="before-str"></a>

A cursor for use in pagination. ```before``` is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, starting with ```obj_bar```, your subsequent call can include ```before=obj_bar``` in order to fetch the previous page of the list.

##### after: `str`<a id="after-str"></a>

A cursor for use in pagination. after is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bank-transfer-payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.itp.create_payment_instruction`<a id="sqalaitpcreate_payment_instruction"></a>

Create an ITP

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_payment_instruction_response = sqala.itp.create_payment_instruction(
    amount=1,
    payer={},
    code="string_example",
    split=[
        {
            "value": 1,
            "recipient_id": "recipient_id_example",
        }
    ],
    metadata=[{}],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

Amount in cents to be paid.

##### payer: [`ItpCreatePaymentInstructionRequestPayer`](./sqala_python_sdk/type/itp_create_payment_instruction_request_payer.py)<a id="payer-itpcreatepaymentinstructionrequestpayersqala_python_sdktypeitp_create_payment_instruction_request_payerpy"></a>


##### code: `str`<a id="code-str"></a>

Unique identifier for the object in your system.

##### split: [`ItpCreatePaymentInstructionRequestSplit`](./sqala_python_sdk/type/itp_create_payment_instruction_request_split.py)<a id="split-itpcreatepaymentinstructionrequestsplitsqala_python_sdktypeitp_create_payment_instruction_request_splitpy"></a>

##### metadata: [`ItpCreatePaymentInstructionRequestMetadata`](./sqala_python_sdk/type/itp_create_payment_instruction_request_metadata.py)<a id="metadata-itpcreatepaymentinstructionrequestmetadatasqala_python_sdktypeitp_create_payment_instruction_request_metadatapy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ItpCreatePaymentInstructionRequest`](./sqala_python_sdk/type/itp_create_payment_instruction_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ItpCreatePaymentInstructionResponse`](./sqala_python_sdk/pydantic/itp_create_payment_instruction_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/itp-payments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.itp.get_itp`<a id="sqalaitpget_itp"></a>

Retrieve an ITP

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_itp_response = sqala.itp.get_itp(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Unique identifier for the object.

#### 🔄 Return<a id="🔄-return"></a>

[`ItpGetItpResponse`](./sqala_python_sdk/pydantic/itp_get_itp_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/itp-payments/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.itp.list_all`<a id="sqalaitplist_all"></a>

List all ITPs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = sqala.itp.list_all(
    limit=10,
    before="string_example",
    after="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

A limit on the number of objects to be returned, between 1 and 50.

##### before: `str`<a id="before-str"></a>

A cursor for use in pagination. ```before``` is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, starting with ```obj_bar```, your subsequent call can include ```before=obj_bar``` in order to fetch the previous page of the list.

##### after: `str`<a id="after-str"></a>

A cursor for use in pagination. after is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`ItpListAllResponse`](./sqala_python_sdk/pydantic/itp_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/itp-payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.qr_code.generate_qr_code`<a id="sqalaqr_codegenerate_qr_code"></a>

Create a Pix QR Code

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_qr_code_response = sqala.qr_code.generate_qr_code(
    amount=1,
    code="string_example",
    payer={},
    split=[
        {
            "value": 1,
            "recipient_id": "recipient_id_example",
        }
    ],
    metadata=[{}],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

Amount in cents to be paid.

##### code: `str`<a id="code-str"></a>

Unique identifier for the object in your system.

##### payer: [`QrCodeGenerateQrCodeRequestPayer`](./sqala_python_sdk/type/qr_code_generate_qr_code_request_payer.py)<a id="payer-qrcodegenerateqrcoderequestpayersqala_python_sdktypeqr_code_generate_qr_code_request_payerpy"></a>


##### split: [`QrCodeGenerateQrCodeRequestSplit`](./sqala_python_sdk/type/qr_code_generate_qr_code_request_split.py)<a id="split-qrcodegenerateqrcoderequestsplitsqala_python_sdktypeqr_code_generate_qr_code_request_splitpy"></a>

##### metadata: [`QrCodeGenerateQrCodeRequestMetadata`](./sqala_python_sdk/type/qr_code_generate_qr_code_request_metadata.py)<a id="metadata-qrcodegenerateqrcoderequestmetadatasqala_python_sdktypeqr_code_generate_qr_code_request_metadatapy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`QrCodeGenerateQrCodeRequest`](./sqala_python_sdk/type/qr_code_generate_qr_code_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`QrCodeGenerateQrCodeResponse`](./sqala_python_sdk/pydantic/qr_code_generate_qr_code_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pix-qrcode-payments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.qr_code.get_qr_code_by_id`<a id="sqalaqr_codeget_qr_code_by_id"></a>

Retrieve a Pix QR Code

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_qr_code_by_id_response = sqala.qr_code.get_qr_code_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Unique identifier for the object.

#### 🔄 Return<a id="🔄-return"></a>

[`QrCodeGetQrCodeByIdResponse`](./sqala_python_sdk/pydantic/qr_code_get_qr_code_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pix-qrcode-payments/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.qr_code.list_all`<a id="sqalaqr_codelist_all"></a>

List all Pix QR Codes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = sqala.qr_code.list_all(
    limit=10,
    before="string_example",
    after="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

A limit on the number of objects to be returned, between 1 and 50.

##### before: `str`<a id="before-str"></a>

A cursor for use in pagination. ```before``` is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, starting with ```obj_bar```, your subsequent call can include ```before=obj_bar``` in order to fetch the previous page of the list.

##### after: `str`<a id="after-str"></a>

A cursor for use in pagination. after is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`QrCodeListAllResponse`](./sqala_python_sdk/pydantic/qr_code_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pix-qrcode-payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.recipient.create_bank_account`<a id="sqalarecipientcreate_bank_account"></a>

Create a Bank Account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_bank_account_response = sqala.recipient.create_bank_account(
    holder_name="string_example",
    holder_tax_id="string_example",
    holder_type="INDIVIDUAL",
    branch_number="string_example",
    account_number="string_example",
    bank_id="string_example",
    recipient_id="DEFAULT",
    type="CHECKING",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### holder_name: `str`<a id="holder_name-str"></a>

The name of the person or business that owns the bank account.

##### holder_tax_id: `str`<a id="holder_tax_id-str"></a>

The tax ID of the account holder (CPF for individual account holders or CNPJ for businesses account holders).

##### holder_type: `str`<a id="holder_type-str"></a>

The type of entity that holds the account. Can be INDIVIDUAL or COMPANY.

##### branch_number: `str`<a id="branch_number-str"></a>

##### account_number: `str`<a id="account_number-str"></a>

##### bank_id: `str`<a id="bank_id-str"></a>

The ID of the bank associated with the account.

##### recipient_id: `str`<a id="recipient_id-str"></a>

##### type: `str`<a id="type-str"></a>

The type of bank account. Can be CHEKING or SAVINGS.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RecipientCreateBankAccountRequest`](./sqala_python_sdk/type/recipient_create_bank_account_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RecipientCreateBankAccountResponse`](./sqala_python_sdk/pydantic/recipient_create_bank_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recipients/{recipientId}/bank-accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.recipient.create_recipient`<a id="sqalarecipientcreate_recipient"></a>

Create a Recipient

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_recipient_response = sqala.recipient.create_recipient(
    name="string_example",
    tax_id="string_example",
    type="INDIVIDUAL",
    code="string_example",
    metadata=[{}],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the recipient.

##### tax_id: `str`<a id="tax_id-str"></a>

The tax ID of the recipient (CPF for individual recipients or CNPJ for businesses recipients).

##### type: `str`<a id="type-str"></a>

The type of the recipient.

##### code: `str`<a id="code-str"></a>

Unique identifier for the object in your system.

##### metadata: [`RecipientCreateRecipientRequestMetadata`](./sqala_python_sdk/type/recipient_create_recipient_request_metadata.py)<a id="metadata-recipientcreaterecipientrequestmetadatasqala_python_sdktyperecipient_create_recipient_request_metadatapy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RecipientCreateRecipientRequest`](./sqala_python_sdk/type/recipient_create_recipient_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recipients` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.recipient.create_withdrawal`<a id="sqalarecipientcreate_withdrawal"></a>

Create a Withdrawal

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_withdrawal_response = sqala.recipient.create_withdrawal(
    amount=1,
    method="STANDARD",
    recipient_id="DEFAULT",
    code="string_example",
    pix_key="string_example",
    bank_account={
        "type": "CHECKING",
        "holder_name": "holder_name_example",
        "holder_tax_id": "holder_tax_id_example",
        "holder_type": "INDIVIDUAL",
        "branch_number": "branch_number_example",
        "account_number": "account_number_example",
        "bank_id": "bank_id_example",
    },
    bank_account_id="string_example",
    metadata=[{}],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

Amount in cents to be transferred.

##### method: `str`<a id="method-str"></a>

The method of the withdrawal.

##### recipient_id: `str`<a id="recipient_id-str"></a>

##### code: `str`<a id="code-str"></a>

Unique identifier for the object in your system.

##### pix_key: `str`<a id="pix_key-str"></a>

The PIX key of the destination bank account. Required if method is PIX

##### bank_account: [`RecipientCreateWithdrawalRequestBankAccount`](./sqala_python_sdk/type/recipient_create_withdrawal_request_bank_account.py)<a id="bank_account-recipientcreatewithdrawalrequestbankaccountsqala_python_sdktyperecipient_create_withdrawal_request_bank_accountpy"></a>


##### bank_account_id: `str`<a id="bank_account_id-str"></a>

The ID of the destination bank account. Required if method is STANDARD.

##### metadata: [`RecipientCreateWithdrawalRequestMetadata`](./sqala_python_sdk/type/recipient_create_withdrawal_request_metadata.py)<a id="metadata-recipientcreatewithdrawalrequestmetadatasqala_python_sdktyperecipient_create_withdrawal_request_metadatapy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RecipientCreateWithdrawalRequest`](./sqala_python_sdk/type/recipient_create_withdrawal_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RecipientCreateWithdrawalResponse`](./sqala_python_sdk/pydantic/recipient_create_withdrawal_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recipients/{recipientId}/withdrawals` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.recipient.delete_bank_account`<a id="sqalarecipientdelete_bank_account"></a>

Delete a Bank Account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_bank_account_response = sqala.recipient.delete_bank_account(
    recipient_id="DEFAULT",
    bank_account_id="bankAccountId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recipient_id: `str`<a id="recipient_id-str"></a>

##### bank_account_id: `str`<a id="bank_account_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RecipientDeleteBankAccountResponse`](./sqala_python_sdk/pydantic/recipient_delete_bank_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recipients/{recipientId}/bank-accounts/{bankAccountId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.recipient.get_balance`<a id="sqalarecipientget_balance"></a>

Get Balance

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_balance_response = sqala.recipient.get_balance(
    recipient_id="DEFAULT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recipient_id: `str`<a id="recipient_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recipients/{recipientId}/balance` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.recipient.get_bank_account`<a id="sqalarecipientget_bank_account"></a>

Retrieve a Bank Account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bank_account_response = sqala.recipient.get_bank_account(
    recipient_id="DEFAULT",
    bank_account_id="bankAccountId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recipient_id: `str`<a id="recipient_id-str"></a>

##### bank_account_id: `str`<a id="bank_account_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RecipientGetBankAccountResponse`](./sqala_python_sdk/pydantic/recipient_get_bank_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recipients/{recipientId}/bank-accounts/{bankAccountId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.recipient.get_by_id`<a id="sqalarecipientget_by_id"></a>

Retrieve a Recipient

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = sqala.recipient.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recipients/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.recipient.get_withdrawal_by_id`<a id="sqalarecipientget_withdrawal_by_id"></a>

Retrieve a Withdrawal

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_withdrawal_by_id_response = sqala.recipient.get_withdrawal_by_id(
    recipient_id="DEFAULT",
    withdrawal_id="withdrawalId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recipient_id: `str`<a id="recipient_id-str"></a>

##### withdrawal_id: `str`<a id="withdrawal_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RecipientGetWithdrawalByIdResponse`](./sqala_python_sdk/pydantic/recipient_get_withdrawal_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recipients/{recipientId}/withdrawals/{withdrawalId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.recipient.list_all`<a id="sqalarecipientlist_all"></a>

List all Recipients

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = sqala.recipient.list_all(
    limit=10,
    before="string_example",
    after="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

A limit on the number of objects to be returned, between 1 and 50.

##### before: `str`<a id="before-str"></a>

A cursor for use in pagination. ```before``` is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, starting with ```obj_bar```, your subsequent call can include ```before=obj_bar``` in order to fetch the previous page of the list.

##### after: `str`<a id="after-str"></a>

A cursor for use in pagination. after is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`RecipientListAllResponse`](./sqala_python_sdk/pydantic/recipient_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recipients` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.recipient.list_bank_accounts`<a id="sqalarecipientlist_bank_accounts"></a>

List all Bank Accounts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_bank_accounts_response = sqala.recipient.list_bank_accounts(
    recipient_id="DEFAULT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recipient_id: `str`<a id="recipient_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RecipientListBankAccountsResponse`](./sqala_python_sdk/pydantic/recipient_list_bank_accounts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recipients/{recipientId}/bank-accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.recipient.list_transactions`<a id="sqalarecipientlist_transactions"></a>

List all Transactions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_transactions_response = sqala.recipient.list_transactions(
    recipient_id="DEFAULT",
    limit="10",
    before="string_example",
    after="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recipient_id: `str`<a id="recipient_id-str"></a>

##### limit: `str`<a id="limit-str"></a>

A limit on the number of objects to be returned, between 1 and 50.

##### before: `str`<a id="before-str"></a>

A cursor for use in pagination. ```before``` is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, starting with ```obj_bar```, your subsequent call can include ```before=obj_bar``` in order to fetch the previous page of the list.

##### after: `str`<a id="after-str"></a>

A cursor for use in pagination. after is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recipients/{recipientId}/transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.recipient.list_withdrawals`<a id="sqalarecipientlist_withdrawals"></a>

List all Withdrawals

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_withdrawals_response = sqala.recipient.list_withdrawals(
    recipient_id="DEFAULT",
    limit="10",
    before="string_example",
    after="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recipient_id: `str`<a id="recipient_id-str"></a>

##### limit: `str`<a id="limit-str"></a>

A limit on the number of objects to be returned, between 1 and 50.

##### before: `str`<a id="before-str"></a>

A cursor for use in pagination. ```before``` is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, starting with ```obj_bar```, your subsequent call can include ```before=obj_bar``` in order to fetch the previous page of the list.

##### after: `str`<a id="after-str"></a>

A cursor for use in pagination. after is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`RecipientListWithdrawalsResponse`](./sqala_python_sdk/pydantic/recipient_list_withdrawals_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recipients/{recipientId}/withdrawals` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.recipient.update_recipient_by_id`<a id="sqalarecipientupdate_recipient_by_id"></a>

Update a Recipient

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_recipient_by_id_response = sqala.recipient.update_recipient_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recipients/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.token.generate_access_token`<a id="sqalatokengenerate_access_token"></a>

Create an Access Token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_access_token_response = sqala.token.generate_access_token(
    refresh_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### refresh_token: `str`<a id="refresh_token-str"></a>

The Refresh Token is used to get a new Access Token, when the old one expires.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TokenGenerateAccessTokenRequest`](./sqala_python_sdk/type/token_generate_access_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TokenGenerateAccessTokenResponse`](./sqala_python_sdk/pydantic/token_generate_access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/access-tokens` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.webhook.get`<a id="sqalawebhookget"></a>

Retrieve a Webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = sqala.webhook.get(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookGetResponse`](./sqala_python_sdk/pydantic/webhook_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.webhook.list_all`<a id="sqalawebhooklist_all"></a>

List all Webhooks

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = sqala.webhook.list_all(
    status="PENDING",
    event="string_example",
    endpoint_id="string_example",
    limit=10,
    before="string_example",
    after="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

##### event: `str`<a id="event-str"></a>

##### endpoint_id: `str`<a id="endpoint_id-str"></a>

##### limit: `int`<a id="limit-int"></a>

A limit on the number of objects to be returned, between 1 and 50.

##### before: `str`<a id="before-str"></a>

A cursor for use in pagination. ```before``` is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, starting with ```obj_bar```, your subsequent call can include ```before=obj_bar``` in order to fetch the previous page of the list.

##### after: `str`<a id="after-str"></a>

A cursor for use in pagination. after is an object ID that defines your place in the list. For instance, if you make a list request and receive 50 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookListAllResponse`](./sqala_python_sdk/pydantic/webhook_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sqala.webhook.resend_attempt`<a id="sqalawebhookresend_attempt"></a>

Resend a Webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
resend_attempt_response = sqala.webhook.resend_attempt(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookResendAttemptResponse`](./sqala_python_sdk/pydantic/webhook_resend_attempt_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{id}/attempts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
