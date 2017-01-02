import collections,sys,re,Queue
# transitions = collections.defaultdict(set)

def expand_iter(input):
    for src in transitions:
        for dst in transitions[src]:
            for match in re.finditer(src, input):
                yield input[:match.start()] + dst + input[match.end():]

# expansions = set(expand_iter(target))

# print(len(expansions))

transitions = {}

f=open ('day19.txt','r')

for i in xrange(43):
    src,dst=f.readline().strip().split(' => ')
    transitions[dst] = src

f.readline()
target = f.readline().strip()

def build_iter(input):
    for dst in transitions:
        src = transitions[dst]
        for match in re.finditer(dst, input):
            yield input[:match.start()] + src + input[match.end():]

q = Queue.PriorityQueue()
q.put((len(target), 0, target))

while True:
    length, iterations, current = q.get()

    if current == 'e':
        break

    for precursor in build_iter(current):
        q.put((len(precursor), iterations + 1, precursor))

print(iterations)