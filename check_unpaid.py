def check_unpaid(tenant_name, months):
    if months >= 3:
        print(tenant_name + ":" + "督促状を送付")
    elif months >= 1:
        print(tenant_name + ":" + "リマインドを送付")
    else:
        print(tenant_name + ":" + "対応不要")

check_unpaid("田中", 3)
check_unpaid("佐藤", 1)
check_unpaid("鈴木", 0)
