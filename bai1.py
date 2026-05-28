cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

check = True

while check:
    menu = """
    ==================================================
            SHOPEE CART MANAGEMENT SYSTEM
    ==================================================
    1. Xem chi tiết giỏ hàng & Tính tổng tiền
    2. Thêm sản phẩm mới / Cộng dồn số lượng
    3. Cập nhật số lượng của một sản phẩm
    4. Xóa sản phẩm khỏi giỏ hàng
    5. Thoát chương trình
    ==================================================
    """
    print(menu)
    
    choice_str = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
    match choice_str:
        case "1":
            print("\n---- CHI TIẾT GIỎ HÀNG ----")
            if len(cart_items) == 0:
                print("Giỏ hàng của bạn hiện đang trống!")
            else:
                print(f"{'STT':<4}| {'Mã SP':<6}| {'Tên Sản Phẩm':<25} | {'SL':<3} | {'Đơn Giá':<12} | {'Thành Tiền'}")
                print("-" * 72)
                
                tong_so_luong = 0
                tong_tien = 0
                stt = 1
                
                for item in cart_items:
                    id = item[0]
                    name = item[1]
                    quantity = item[2]
                    price = item[3]
                    
                    total_price = quantity * price
                    
                    tong_so_luong = tong_so_luong + quantity
                    tong_tien = tong_tien + total_price
                    
                    print(f"{stt:<4}| {id:<6}| {name:<25} | {quantity:<3} | {price:<12,}đ | {total_price:,}đ")
                    stt = stt + 1
                
                print("-" * 72)
                print(f"=> Tổng số lượng sản phẩm trong giỏ: {tong_so_luong}")
                print(f"=> TỔNG TIỀN THANH TOÁN: {tong_tien:,}đ")
            print()
            
        case "2":
            insert_order = input("Nhập mã sản phẩm: ").strip().upper()
            name = input("Nhập tên sản phẩm: ").strip()
            
            quantity_str = input("Nhập số lượng: ").strip()
            price_str = input("Nhập đơn giá: ").strip()
            
            if not quantity_str.isdigit() or not price_str.isdigit():
                print("Lỗi: Số lượng và đơn giá phải là các ký tự số nguyên hợp lệ!")
                print()
                continue
                
            quantity = int(quantity_str)
            price = int(price_str)
            
            if quantity <= 0 or price < 0:
                print("Lỗi: Số lượng phải lớn hơn 0 và đơn giá không được nhỏ hơn 0!")
                print()
                continue
                
            da_trung = False
            for item in cart_items:
                if item[0] == insert_order:
                    item[2] = item[2] + quantity
                    da_trung = True
                    print(f"Sản phẩm {insert_order} đã tồn tại. Cộng dồn số lượng thành công!")
                    break
            
            if da_trung == False:
                cart_items.append([insert_order, name, quantity, price])
                print(f"Đã thêm mới sản phẩm {insert_order} vào giỏ hàng thành công!")
            print()
            
        case "3":
            insert_order = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
            
            danh_sach_ma = [item[0] for item in cart_items]
            if insert_order not in danh_sach_ma:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")
                print()
                continue
                
            quantity_str = input("Nhập số lượng mới cần thay đổi: ").strip()
            if not quantity_str.isdigit():
                print("Lỗi: Số lượng nhập vào phải là số nguyên!")
                print()
                continue
                
            quantity_moi = int(quantity_str)
            
            if quantity_moi <= 0:
                print("Lỗi: Số lượng cập nhật phải lớn hơn 0!")
                print()
                continue
                
            for item in cart_items:
                if item[0] == insert_order:
                    item[2] = quantity_moi
                    print(f"Đã cập nhật số lượng cho sản phẩm {insert_order} thành công.")
                    break
            print()
            
        case "4":
            insert_order = input("Nhập mã sản phẩm muốn xóa khỏi giỏ hàng: ").strip().upper()
            
            tim_thay = False
            for index in range(len(cart_items)):
                if cart_items[index][0] == insert_order:
                    san_pham_xoa = cart_items.pop(index)
                    print(f"Đã xóa hoàn toàn sản phẩm khỏi giỏ hàng: {san_pham_xoa[1]} ({san_pham_xoa[0]})")
                    tim_thay = True
                    break
                    
            if tim_thay == False:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")
            print()
            
        case "5":
            print("Đã thoát chương trình!")
            check = False
            
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 5!")
            print()