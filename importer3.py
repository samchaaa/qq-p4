from sklearn.externals import joblib

class ImporterClass():

    def __init__(self):

        pass

    def ImporterFunction(self):

        asdf = joblib.load('./model_AGG.sav')

        return asdf
