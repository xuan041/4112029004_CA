books_stock = [{"書名":"書籍1", "價格": 100, "庫存":2},
               {"書名":"書籍2", "價格": 200, "庫存":4},
               {"書名":"書籍3", "價格": 300, "庫存":6},
               {"書名":"書籍4", "價格": 400, "庫存":8} ]

while True :
    move = input("請輸入要做的事項:")
    if(move == "添加書籍"):
        add_book_name = input("要新增書籍之名稱：")
        add_book_price = int(input("要新增書籍之價格："))
        add_book_stock = int(input("要新增書籍之庫存："))
        books_stock.append({"書名":add_book_name, "價格": add_book_price, "庫存": add_book_stock})
        print(f"書籍'{add_book_name}'已成功加入庫存！")

    if(move == "顯示庫存"):
        for i in range (len(books_stock)):
          pick = books_stock[i]
          print(f"書名：{pick['書名']}, 價格：{pick['價格']}, 庫存：{pick['庫存']} ")
    if(move == "刪除書籍"):
        del_book = input("請輸入要刪除之書籍：")
        for i in range (len(books_stock)):
          pick = books_stock[i]
          if(pick["書名"] == del_book):
            del books_stock[i]
            break
        print(f"書籍'{del_book}'已成功從庫存中移除！")
    if(move == "更新庫存"):
        stock_book = input("請輸入要更改庫存之書籍名：")
        for i in range(len(books_stock)):
          pick = books_stock[i]
          if(pick["書名"] == stock_book):
            quantity = input(f"請輸入要將{stock_book}之庫存改為：")
            pick["庫存"] = quantity
        print(f"書籍'{stock_book}'的庫存已經更新為{quantity}本！")







