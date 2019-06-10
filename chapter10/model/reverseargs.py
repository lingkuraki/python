import sys

print(sys.argv)
args = sys.argv[1:]
args.reverse()
print(' '.join(args))
