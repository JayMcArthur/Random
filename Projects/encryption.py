import hashlib, base64
def main() -> None:
    salt = 'W1CKIlzp7oU'
    id = 'quiz'
    hash = hashlib.sha256(f'{id}{salt}'.encode('utf8'))
    result = base64.b64encode(hash.digest()).decode()
    print(result)
