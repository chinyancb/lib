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

        self.f.write(message)

    
    """
    debug
    @access public
    @param：message ログ出力内容
    @return :　正常系：True
            ： 異常系：False
    """
    def debug(self, message):

        level = self.logLevel['debug']
        result = self.__write(level, message)
