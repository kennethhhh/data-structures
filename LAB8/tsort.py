from sys import argv
from stack_array import *

def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''

    #dictionary[vertex][0] is the in degree
    #dictionary[vertex][1:] is the vertices adjacent to dictionary[vertex]
    dictionary={}
    order_list=[]
    string=''
    if len(vertices)==0:
        raise ValueError("input contains no edges")
    if len(vertices)%2==1:
        raise ValueError("input contains an odd number of tokens")

    #creating dictionary
    for index in range(0,len(vertices),2):
        if vertices[index] not in order_list:
            order_list.append(vertices[index])
        if vertices[index] in dictionary:
            #adding vertex2 adjacent to vertex1 to the list
            dictionary[vertices[index]].append(vertices[index+1])
            # adds 1 to in degree of adjacent vertex
            if vertices[index + 1] not in dictionary:
                dictionary[vertices[index + 1]] = [1]
            # creates vertex and makes in degree 1
            else:
                dictionary[vertices[index + 1]][0] += 1
        else:
            dictionary[vertices[index]]=[0,vertices[index+1]]
            #adds 1 to in degree of adjacent vertex
            if vertices[index+1] not in dictionary:
                dictionary[vertices[index + 1]] = [1]
            #creates vertex and makes in degree 1
            else:
                dictionary[vertices[index + 1]][0] += 1


    stack = Stack(len(vertices))
    #initial push
    for item in order_list:
        if dictionary[item][0]==0:
            stack.push(item)

    #during tsort
    while stack.num_items!=0:
        temp=stack.pop()
        string+=temp+'\n'
        adjacent=dictionary[temp][1:]
        for vertex in adjacent:
            dictionary[vertex][0]-=1
            if dictionary[vertex][0]==0:
                stack.push(vertex)

    if len(string.split())!=len(dictionary):
        raise ValueError("input contains a cycle")

    return string.strip()




#tsort(['101', '102', '102', '103', '103', '315', '225', '315', '103', '357', '315', '357', '141', '102', '102', '225'])
#tsort(['1', '2', '1', '9', '1', '8', '9', '8', '9', '10', '8', '11', '10', '11', '2', '3', '3', '11', '3', '4', '4', '7', '4', '5', '7', '5', '7', '13', '7', '6', '6', '14', '6', '12'])

def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()

    vertices = []
    for line in f:
        vertices += line.split()

    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
