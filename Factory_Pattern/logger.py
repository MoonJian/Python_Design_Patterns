from abc import abstractmethod

class Logger():
    @abstractmethod
    def writelog(self):
        pass

class DataBaseLogger(Logger):
    def writelog(self):
        print("DataBase Logger!")

class FileLogger(Logger):
    def writelog(self):
        print("File Logger!")

class LoggerFactory():
    @abstractmethod
    def createLogger(self):
        pass

class DataBaseLoggerFactory(LoggerFactory):
    def createLogger(self):
        logger = DataBaseLogger()
        return logger

class FileLoggerFactory(LoggerFactory):
    def createLogger(self):
        logger = FileLogger()
        return logger


if __name__ == '__main__':
    factory = FileLoggerFactory()
    logger = factory.createLogger()
    logger.writelog()