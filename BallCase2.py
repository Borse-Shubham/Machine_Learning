from sklearn import tree

def main():
    print("Ball Classification Case Study")

    # Load the data
    BallFeatures = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1], [92,0],[35,1],[35,1],[35,1], [96,0], [43,1],[110,0], [35,1],[95,0]]

    Labels = ["Teenis", "Tennis", "Cricket","Tennis", "Cricket", "Tennis","Cricket", "Tennis","Tennis", "Tennis","Cricket", "Tennis", "Cricket","Tennis","Cricket"]

    obj = tree.DecisionTreeClassifier()     # Decide the algorithm

    obj = obj.fit(BallFeatures,Labels)      # Train the model

    print(obj.predict([[39,1], [89,0]]))   # Test the model

if __name__ == "__main__":
    main()