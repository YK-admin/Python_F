class HelloWorld:
    __slots__ = "message"

    def __init__(self) -> None:
        """コンストラクタ"""
        self.message = "Hello, World!"

    def defaultPrint(self):
        """インスタンス変数のmessageを表示"""
        print(self.message, end="")

    def english(self):
        """英語版hello worldを返す"""
        self.message = "Hello, World!"
        return self.message
    
    def printEnglish(self):
        """英語版hello world表示"""
        self.english()
        print(self.message, end="")

    def french(self):
        """フランス語版hello worldを返す"""
        self.message = "Bonjour le monde!"
        return self.message
    
    def printFrench(self):
        """フランス語版hello world表示"""
        self.french()
        print(self.message, end="")

    def german(self):
        """ドイツ語版hello worldを返す"""
        self.message = "Hallo Welt!"
        return self.message
    
    def printGerman(self):
        """ドイツ語版hello world表示"""
        self.german()
        print(self.message, end="")

    def spanish(self):
        """スペイン語版hello worldを返す"""
        self.message = "Hola Mundo!"
        return self.message

    def printSpanish(self):
        """スペイン語版hello world表示"""
        self.spanish()
        print(self.message, end="")

    def korean(self):
        """韓国語版hello worldを返す"""
        self.message = "안녕하세요!"
        return self.message
    
    def printKorean(self):
        """韓国語版hello world表示"""
        self.korean
        print(self.message, end="")

    def chinease(self):
        """中国語版hello worldを返す"""
        self.message = "你好 世界!"
        return self.message
    
    def printChinease(self):
        """中国語版hello world表示"""
        self.chinease()
        print(self.message, end="")
    
    def japanease(self):
        """日本語版hello worldを返す"""
        self.message = "こんにちは世界!"
        return self.message
    
    def printJapanease(self):
        """日本語版hello world表示"""
        self.japanease()
        print(self.message, end="")


if __name__=="__main__":
    # HelloWorldインスタンス作成
    helloworld = HelloWorld()

    # HelloWorldを英語で実行
    helloworld.printEnglish()