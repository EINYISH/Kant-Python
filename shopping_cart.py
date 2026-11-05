# shopping cart 클래스 선언
class ShoppingCart:
    def __init__(self):
        self.bucket = []

# 상품 목록 저장 기능
    # 메서드
    # 장바구니 담기
    def add_items(self, item):
        self.bucket.append(item)
    # 장바구니 빼기
    def remove_items(self, item):
        self.bucket.remove(item)
    # 상품 목록 조회
    def show_items(self):
        return self.bucket

# 상품 클래스
class Item:
    def __init__(self, name, price):
        # 속성
        # - 제품명
        self.name = name
        # - 가격
        self.price = price
        

# 쇼핑 카트 생성
cart = ShoppingCart()
# 상품 3개 생성
item_a = Item('초코파이', 12000)
item_b = Item('새우깡', 3000)
item_c = Item('빅파이', 2000)

# 상품 1개 장바구니 담기
cart.add_items(item_a)
# 상품 1개 장바구니 담기
cart.add_items(item_b)
# 상품 1개 장바구니 담기
cart.add_items(item_c)
# 상품 1개 장바구니에서 빼기
cart.remove_items(item_b)
# 장바구니에 담긴 상품 목록 조회
for item in cart.show_items():
    print(item.name, item.price)