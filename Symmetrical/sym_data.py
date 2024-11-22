import os

def get_test_strings():
    return [
        b"What's up?",
        b"Hey, ever meet a fellow by the name of Hill?",
        b"He's a music man, he's a what? He's a music man and he plays clarinets with the kids in the town. " * 10
    ]

def get_random_data():
    return [
        os.urandom(1024),  # 1 KB
        os.urandom(10240),  # 10 KB
        os.urandom(102400)  # 100 KB
    ]

def collect_test_data():
    return get_test_strings() + get_random_data()
