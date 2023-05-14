#"Máy bay nào đến thành phô Huế lúc 13:30HR ?"

class Dictionary:
    def __init__(self):
       
        self.dictionary ={
            "root":"root",
            "?":"?",
            "?.":"?",
            "13:30hr":"mốc thời gian", 
            "1 giơ":"",
            "lúc":"lúc",
            "của":"remove_word",
            "những":"remove_word",
            "các":"remove_word",
            "hãy cho biết":"hãy cho biết",
            "máy bay":"máy bay",
            "nào":"nào",
            "thành phố":"thành phố",
            #"tp.":"thành phố",
            "đà nẵng":"tên thành phố",
            "tp. hồ chí minh":"tên thành phố",
            "hà nội":"tên thành phố",
            "huế":"tên thành phố",
            "tp. hà nội":"tên thành phố",
            "khánh hòa":"tên thành phố", 
            "hải phòng":"tên thành phố",
            "đến":"đến",
            "bay":"bay",
            "xuất phát":"xuất phát",
            "mã hiệu":"mã hiệu",
            "vn4":"mã chuyến bay", 
            "vj5":"mã chuyến bay", 
            "vietjet air":"tên hãng hàng không",
            "hãng hàng không":"hãng hàng không",
            "từ":"từ",
            "thời gian":"remove_word",
            # "mất mấy giờ":"mất mấy giờ",
            "mất":"remove_word",
            "mấy giờ":"mất mấy giờ",
            "1 giờ":"khoảng thời gian",
            "có":"remove_word", 
            "không":"remove_word",
            "hạ cánh":"hạ cánh",
            "ở":"ở",
        }
    def get_dict(self):
        return self.dictionary
    

