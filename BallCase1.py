from sklearn import *

def main():
    print("Ball Classification Case study")

    BallFeatures =[[35,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rough"],[90,"Smooth"]] 

    Labels = ["Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket","Tennis","Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket"]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(BallFeatures,Labels)

    print(obj.predict([36,"Rough"],[91,"Smooth"]))
if __name__=="__main__":
    main()