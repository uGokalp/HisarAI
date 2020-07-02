

def load_titanic() -> tuple:
    """
    Loads preprocessed titanic
    """
    import seaborn as sns
    import pandas as pd
    cols = ['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'alone']
    df = sns.load_dataset('titanic')[cols]
    df.sex = df.sex.astype('category')
    df.alone = df.alone.astype('category')
    df.pclass = df.pclass.astype('category')
    df.parch = df.parch.astype('category')
    df.sibsp = df.sibsp.astype('category')
    df.age = df.age.fillna(df.age.median(skipna=True))
    df = pd.get_dummies(df)
    return df.drop("survived",axis=1), df.survived