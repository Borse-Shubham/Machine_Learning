from sklearn import *

def main():
    print("Ball Classification Case study")

    BallFeatures =[[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 

    Labels = ["Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket","Tennis","Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket"]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(BallFeatures,Labels)

    print(obj.predict([36,0],[91,1]))
if __name__=="__main__":
    main()
    