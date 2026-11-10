class Product:
    number = 0

    def __init__(self, name, price, qty):
        Product.number += 1
        self.id = Product.number
        self.name = name
        self.price = price
        self.qty = qty

    def __str__(self):
        if self.qty == 0:
            return f"{self.id}. {self.name}   {self.price}원  (품절)"
        return f"{self.id}. {self.name}   {self.price}원  (재고{self.qty}개)"

class Mall:
    def __init__(self):
        self.products = []

    # 몰에 상품 등록 함수
    def add_product(self, product):
        self.products.append(product)

    # 상품 목록 함수
    def show_product(self):
        for p in self.products:
            print(p)

class Basket:
    def __init__(self, mall, coupon):
        # 장바구니에 담을 리스트
        self.mall = mall
        self.coupon = coupon
        self.items = []

    def add_to_basket(self):
        # 상품 번호 입력
        product_id = int(input("상품 번호: "))
        target_product = self.mall.products[product_id -1]

        # 재고가 없을 경우
        if target_product.qty == 0:
            print("품절된 상품입니다. ")
            return

        #수량 입력
        count = int(input("수량 : "))

        # count보다 재고가 적을 경우
        if target_product.qty < count:
            print(f"재고가 부족합니다. (담을 수 있는 수량: {target_product.qty}개)")
            return
        
        target_product.qty -= count

        self.items.append((product_id, target_product, count))
        print(f"{target_product.name} {count}개를 담았습니다.")

    def remove_from_basket(self):
        # 상품 번호 입력
        product_id = int(input("상품 번호: "))
        target_product = self.mall.products[product_id -1]

        
        # 상품 번호에 해당하는 상품을 장바구니에서 제거
        for i in self.items:
            if i[0] == product_id:
                # 몰의 상품의 개수는 원복
                target_product.qty += i[2]
                self.items.remove(i)
                print(f"{target_product.name}를 뺐습니다. ")

    def sum_total(self):
        total = 0
        for item in self.items:
            total += item[1].price * item[2]
        return total

    def show_basket(self):
        total = self.sum_total()

        print("-"*57)
        for item in self.items:
            print(f"{item[1].name} X {item[2]}    {item[1].price * item[2]}원")
        print("-"*57)

        discount = self.coupon.apply_discount(total)
        if self.coupon.code == 2:
            discount_message = "10% 할인 최대 (5,000원)"
        elif self.coupon.code == 3:
            discount_message = "3,000원 할인 (20,000원 이상 구매 시)" 
        else:
            discount_message = ""

        if total - discount >= 30000:
            delivery = 0
        else:
            delivery = 3000

        print(f"상품 합계            {total}원")
        print(f"할인                -{discount}원 {discount_message}")
        print(f"배송비               {delivery}원")
        print(f"결제 금액            {total - discount + delivery}원")

class Coupon:
    def __init__(self, code=1):
        self.code = code

    def show_coupon(self):
        print("1. 쿠폰 없음")
        print("2. 10% 할인 (최대 5,000원)")
        print("3. 3,000원 할인 (20,000원 이상 구매 시))")

    def apply_discount(self, total_price):
        if self.code == 1:
            print("쿠폰이 없습니다. ")
            return 0
        elif self.code == 2:
            print("[10% 할인 (최대 5,000원)] 쿠폰을 적용했습니다. ")
            discount = total_price * (0.1)
            if discount > 5000:
                discount = 5000
            return discount
        elif self.code == 3:
            if total_price < 20000:
                print("20,000원 이상 구매시 사용 가능합니다. ")
                return 0
            print("[3,000원 할인 (20,000원 이상 구매 시 )] 쿠폰을 적용했습니다. ")
            discount = 3000
            return discount
            

#====================================================        

mall = Mall()
coupon = Coupon()
basket = Basket(mall, coupon)

product1 = Product("무선 이어폰", 89000, 3)
product2 = Product("텀블러", 15000, 10)
product3 = Product("보조배터리", 32000, 5)
product4 = Product("마우스패드", 9000, 0)
product5 = Product("USB 허브", 18000, 4)

mall.add_product(product1)
mall.add_product(product2)
mall.add_product(product3)
mall.add_product(product4)
mall.add_product(product5)
    
def show_title():
    print("-" * 57)
    print("1. 상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료")
    print("-" * 57)

def select_menu():
    menu = input("선택: ")
    if menu == 'q':
        print("온라인 쇼핑몰을 종료합니다.")
        return False
    
    menu = int(menu)
    if menu == 1:
        mall.show_product()
    elif menu == 2:
        basket.add_to_basket()
    elif menu == 3:
        basket.remove_from_basket()
    elif menu == 4:
        basket.show_basket()
    elif menu == 5:
        coupon.show_coupon()
        code = int(input("쿠폰 번호: "))
        coupon.code = code
        coupon.apply_discount(basket.sum_total())
    elif menu == 6:
        print("영수증 출력")
        print("결제가 완료되었습니다. 감사합니다!")

def main():
    while True:
        show_title()
        select_menu() 
    
main()