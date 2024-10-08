from setuptools import setup, find_packages

setup(
    name="easy-xedu",
    version="0.2.3",
    packages = find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask",
        "flask-cors",
        "flask-socketio",
        "pysimplegui"
    ],
    python_requires='>=3.6',
    license="MIT",
    description="easy-xedu is a web-based platform for training deep learning models using MMEdu framework.",
    entry_points={'console_scripts': ['easytrain=EasyTrain.run:main','easyconvert=EasyConvert.easyconvert:main']},

    )