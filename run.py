"""Local dev server: python run.py  (set PREP_COMPILER_BACKEND=local to use your own gcc)."""
from prep import create_app

if __name__ == "__main__":
    create_app().run(debug=True, port=5000)
