# coding=utf-8
from datetime import datetime
import codecs

"""
python用ロガークラス
"""
class logger:

    """
    それぞれのログレベルで出力するログレベル
    """
    logLevel = {'crit':'CRIT', 'error':'ERROR', 'warning':'WARN', 'info':'INFO', 'debug':'DEBUG' }
    

    """
    コンストラクタ
    @access：public
    @param：ログファイルの絶対パス
    @return：void
    """
    def __init__(self, path):

        self.file = path

        # ファイルopen
        self.f = codecs.open(self.file, 'a', 'utf-8')


    """
    書き出しメソッド
    @access private
    @param : message ログ出力内容
    @return 正常系：True
            異常系：False
    """
    def __write(self, level, message):

        # 時刻取得
        d = datetime.now()

        # ログフォーマット整形
        logtime = "{0:%a %b %d %X %Y}".format(d)
        logMessage ="{} [{}] {}\n".format(logtime, level, message)

        # 書き出し
        self.f.write(logMessage)

    
    """
    debug
    debugログ出力
    @access public
    @param：message ログ出力内容
    @return :　正常系：True
            ： 異常系：False
    """
    def debug(self, message):

        # ログメッセージが設定されていない場合はエラー
        if message == None:
            return False

        # ログレベル文言を取得
        level = self.logLevel['debug']

        # ログ書き出し
        result = self.__write(level, message)

        # ログ書き出しに失敗した場合
        if result == False:
            return False

        return True



    """
    info
    infoログ出力
    @access public
    @param：message ログ出力内容
    @return :　正常系：True
            ： 異常系：False
    """
    def info(self, message):

        # ログメッセージが設定されていない場合はエラー
        if message == None:
            return False

        # ログレベル文言を取得
        level = self.logLevel['info']

        # ログ書き出し
        result = self.__write(level, message)

        # ログ書き出しに失敗した場合
        if result == False:
            return False

        return True


    """
    warn
    warnログ出力
    @access public
    @param：message ログ出力内容
    @return :　正常系：True
            ： 異常系：False
    """
    def warn(self, message):

        # ログメッセージが設定されていない場合はエラー
        if message == None:
            return False

        # ログレベル文言を取得
        level = self.logLevel['warning']

        # ログ書き出し
        result = self.__write(level, message)

        # ログ書き出しに失敗した場合
        if result == False:
            return False

        return True


    """
    error
    errorログ出力
    @access public
    @param：message ログ出力内容
    @return :　正常系：True
            ： 異常系：False
    """
    def error(self, message):

        # ログメッセージが設定されていない場合はエラー
        if message == None:
            return False

        # ログレベル文言を取得
        level = self.logLevel['error']

        # ログ書き出し
        result = self.__write(level, message)

        # ログ書き出しに失敗した場合
        if result == False:
            return False

        return True


    """
    crit
    critログ出力
    @access public
    @param：message ログ出力内容
    @return :　正常系：True
            ： 異常系：False
    """
    def crit(self, message):

        # ログメッセージが設定されていない場合はエラー
        if message == None:
            return False

        # ログレベル文言を取得
        level = self.logLevel['crit']

        # ログ書き出し
        result = self.__write(level, message)

        # ログ書き出しに失敗した場合
        if result == False:
            return False

        return True


    """
    __del__
    デストラクタ
    ファイルクローズ
    @access：public
    @param：void
    @return：void
    """
    def __del__(self):
        
        self.f.close()

