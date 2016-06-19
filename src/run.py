import sys
from shop import app

def main(argv):
    port=5000
    print('running and listening to %s' % port)
    app.run(debug=True, port=port)

if __name__ == "__main__":
    main(sys.argv)
