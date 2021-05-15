from bisect import bisect_left


# range (a,b]

# nlogn using 
# need to create highest piramid, including all blocks, and on the same level, can not be a space between blocks


blocks = [(1,10),(3,6),(10,17),(2,3),(4,5)]

def print_path(sequence):
    for i in range(len(sequence)-1):
        print(f"K{sequence[i]}",end=",")
    print(f"K{sequence[-1]}.")


# working on reference of blocks array, so I'll return only actual biggest block which has been created
def new_block(blocks,correct_sequence,beginings=None,block_range=None,start=True): # <- creating new biggest block
    if start:
        correct_sequence.append(blocks[0][2])
        block_range = blocks.pop(0) # adding first element
        start = False
        beginings = [block[0] for block in blocks] # becouse, I do not know how to work key in bisect, I create array with only blocks starts

    next_block_index = bisect_left(beginings,block_range[1])
    
    if next_block_index < len(beginings) and beginings[next_block_index] == block_range[1]: # next element starts while actual is ending
        correct_sequence.append(blocks[next_block_index][2])
        block_range = (block_range[0], blocks[next_block_index][1], next_block_index) # resizing actual block
        blocks.pop(next_block_index)
        beginings.pop(next_block_index)
        block_range = new_block(blocks,correct_sequence,beginings,block_range,start)
        
    
        
# need to fall blocks, in correct sequence
def block_merge(blocks):
    correct_sequence = []
    blocks = [(block[0],block[1],i) for i,block in zip(range(len(blocks)),blocks)] # (a,b,index)
    blocks.sort(key=lambda element: element[0])

    while len(blocks) > 0:
        new_block(blocks,correct_sequence)

    print_path(correct_sequence)


block_merge(blocks)