{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4, 5, 6, 7)\n",
      "(2, 'hello', 99, 9)\n"
     ]
    }
   ],
   "source": [
    "# Tuples\n",
    "# Like List You can store a list of data\n",
    "l =(4,5,6,7)\n",
    "print(l)\n",
    "\n",
    "#Like list it can store different type of data int,string, float\n",
    "l2= (2,\"hello\",99,9)\n",
    "print(l2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4848, 4884.994, 'hello')\n"
     ]
    }
   ],
   "source": [
    "#Basic Difference between list & Tuples\n",
    "    #It use's () braces instead of [] brackets\n",
    "l= (4848,4884.994,\"hello\")\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "45\n",
      "45\n"
     ]
    }
   ],
   "source": [
    "# Accessing the index is same as tuple\n",
    "tup =(4,8,99,89,45)\n",
    "print(tup[4])\n",
    "\n",
    "#reverse operation with tuple\n",
    "print(tup[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4, 99)\n",
      "()\n"
     ]
    }
   ],
   "source": [
    "# We can use the same slicing operation as List\n",
    "\n",
    "print(tup[0:4:2])\n",
    "print(tup[0:4:-1]) # its empty becoz as we by default it goes forward but we have put jump by -1 so the pointer it does not move"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-13-02edf81320bf>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# We can paticular index\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[1;31m#Mutablity List allows to update the value at paticular while tuple does NOT\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mtup\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m\u001b[1;36m43\u001b[0m \u001b[1;31m#'tuple' object does not support item assignment  we cannot update\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "# We can paticular index\n",
    "    #Mutablity List allows to update the value at paticular while tuple does NOT\n",
    "tup[3] =43 #'tuple' object does not support item assignment  we cannot update\n",
    "\n",
    "#IN LIST WE CAN UPDATE AT PATICULAR INDEX VALUE\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4444, 'hello', 52, [888, 56, 89, 'hi'])\n"
     ]
    }
   ],
   "source": [
    "# We can create list inside a tuple \n",
    "\n",
    "t = (4444,\"hello\",52,[888,56,89,\"hi\"])\n",
    "print(t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Databases usually returs data as tuples\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{}\n",
      "{4, 5, 9, 44, 77, 89}\n",
      "<class 'set'>\n"
     ]
    }
   ],
   "source": [
    "# SET we can Create Set\n",
    "    # in set we use {} braces\n",
    "    # if its empty show its type dict\n",
    "    # once stored it gives type as set\n",
    "s ={}\n",
    "print(s)\n",
    "s={4,5,9,44,89,77}\n",
    "print(s)\n",
    "print(type(s))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{66, 99, 48, 84, 55}\n",
      "{'hello', 99, 85, 55, 666, 'Hello'}\n"
     ]
    }
   ],
   "source": [
    "#It stores unique values removes duplication\n",
    "s2={55,84,84,99,66,48,55,55,55}\n",
    "print(s2)\n",
    "\n",
    "#It consider case sensitve data as different data so it will give result  for both upper and lower case\n",
    "\n",
    "s3 ={55,\"Hello\",666,85,99,\"hello\",99}\n",
    "print(s3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{79, 22, 55, 88, 26}\n"
     ]
    }
   ],
   "source": [
    "# It shows it sequence Data BUT it does NOT STORE DATA IN SEQUENCE THE INDEX IS DIFFERENT\n",
    "# Is an Unodered collection of DATA\n",
    "\n",
    "s={55,26,88,79,22}\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[88, 99, 55]\n",
      "{88, 99, 55}\n"
     ]
    }
   ],
   "source": [
    "# U CANT ACCESS AT A PATICULAR INDEX\n",
    "#s = s[0]\n",
    "#print(s) # U Cant acess it\n",
    "\n",
    "#if you want to access at paticular index YOU can CONVERT INTO LIST\n",
    "s={55,88,99}\n",
    "l1 =list(s)\n",
    "print(l1)\n",
    "\n",
    "# Again U can store Again into SET\n",
    "s =set(l1)\n",
    "print(s)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'dict'>\n"
     ]
    }
   ],
   "source": [
    "# DICTIONARY DATA TYPE\n",
    "    #IT stores value in KEY VALUE Mannner\n",
    "    \n",
    "d ={}\n",
    "print(type(d))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'Hello', 'Class': '4th Grade', 'Age': 44}\n"
     ]
    }
   ],
   "source": [
    "#Key is moslty in string format\n",
    "d ={\"name\":\"Hello\", \"Class\": \"4th Grade\", \"Age\": 44}\n",
    "print(d)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'hello'}\n"
     ]
    }
   ],
   "source": [
    "#Key Value should be Unique If same IT WILL TAKE LAST VALUE\n",
    "d1 ={\"name\":\"Hi\", \"name\": \"hello\"}\n",
    "print(d1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{252552: 'Hi', 'name': 'hello'}\n"
     ]
    }
   ],
   "source": [
    "#Numeric Value for Key is allowed\n",
    "d1 ={252552:\"Hi\", \"name\": \"hello\"}\n",
    "print(d1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{252552: 'Hi', 'name': 'hello'}\n"
     ]
    }
   ],
   "source": [
    "# it does NOT ALLOW SPECIAL CHARATCER BUT U CAN COVERT into string\n",
    "#d1 ={_252552:\"Hi\", \"name\": \"hello\"} //This will give error\n",
    "\n",
    "d2 ={\"_252552\":\"Hi\", \"name\": \"hello\"}\n",
    "print(d1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'hello', 'Age': 44, 'city': [['delhi', 'bombay'], 66, (22, 23)]}\n"
     ]
    }
   ],
   "source": [
    "# We can even store tuple's, List in dictonary as values  BUT KEY IS NOT ALLOWED in form of list, set,dict\n",
    "\n",
    "a ={\"name\":\"hello\", \"Age\":44, \"city\":[[\"delhi\", \"bombay\"],66,(22,23)]}\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': {1, 2, 3}}\n"
     ]
    }
   ],
   "source": [
    "# We can hold set data in dict as values\n",
    "\n",
    "a ={\"name\":{1,2,3}}\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3}\n"
     ]
    }
   ],
   "source": [
    "# We can not KEEP SAME KEY whereas Values can be duplicate\n",
    "# WE can access value of paticular Index BUT WE NEED TO GIVE KEY TO ACCESS VALUE\n",
    "\n",
    "b={\"name\":{1,2,3} , \"Age\": 44}\n",
    "print(b[\"name\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{(3, 4, 5): 'tuple is key'}\n"
     ]
    }
   ],
   "source": [
    "#Even Tuple can be the KEY\n",
    "d={(3,4,5) : \"tuple is key\"}\n",
    "print (d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unhashable type: 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-52-91c86364d773>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0md\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m:\u001b[0m \u001b[1;34m\"tuple is key\"\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0md\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: unhashable type: 'list'"
     ]
    }
   ],
   "source": [
    "#CANNOT HAVE LIST AS KEY\n",
    "d={[3,4,5] : \"tuple is key\"}\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unhashable type: 'set'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-53-172f589c3892>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0md\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m}\u001b[0m \u001b[1;33m:\u001b[0m \u001b[1;34m\"tuple is key\"\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0md\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: unhashable type: 'set'"
     ]
    }
   ],
   "source": [
    "#CANNOT have SET as KEY\n",
    "d={{3,4,5} : \"tuple is key\"}\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unhashable type: 'set'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-55-2c3dda9addf4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#CANNOT have DICT as KEY\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0md\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;34m\"this is Dict\"\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"hello how\"\u001b[0m \u001b[1;34m\"tuple is key\"\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0md\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: unhashable type: 'set'"
     ]
    }
   ],
   "source": [
    "#CANNOT have DICT as KEY\n",
    "d={{\"this is Dict\"}: \"hello how\" \"tuple is key\"}\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'str' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-58-b22b9e82a77d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#Strings and Tuples are inmutalble means there index's CANNOT be updated by accessing there index\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mstring_value\u001b[0m \u001b[1;33m=\u001b[0m\u001b[1;34m\"hello how r u\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mstring_value\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m\u001b[1;34m\"h\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstring_value\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'str' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "#Strings and Tuples are inmutalble means there index's CANNOT be updated by accessing there index\n",
    "string_value =\"hello how r u\"\n",
    "string_value[0] =\"h\" # This will give erro 'str' object does not support item assignment\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "23"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Accesing the Value of Key and in that if it has a list\n",
    "s = {\"name\":\"hello\", \"Age\":44, \"city\":[[\"delhi\", \"bombay\"],66,(22,23)]}\n",
    "s[\"city\"][0]\n",
    "\n",
    "#Accesing the Value of Key and in that if it has a Tuple\n",
    "s = {\"name\":\"hello\", \"Age\":44, \"city\":[[\"delhi\", \"bombay\"],66,(22,23)]}\n",
    "s[\"city\"][2][1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'set' object is not subscriptable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-64-dfbf0650f923>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;31m#But accessing the value of SET values is not possible as we know the set stores the value not in odered form\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m \u001b[0ms\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"area\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'set' object is not subscriptable"
     ]
    }
   ],
   "source": [
    "#Accesing the Value of Key and in that if it has a list\n",
    "s = {\"name\":\"hello\", \"Age\":44, \"city\":[[\"delhi\", \"bombay\"],66,(22,23)], \"area\":{2,3,4,8}}\n",
    "s[\"area\"]\n",
    "\n",
    "#But accessing the value of SET values is not possible as we know the set stores the value not in odered form\n",
    "s[\"area\"][0] # This will give error 'set' object is not subscriptable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " # IMMUTABLE ELEMENTS CAN BE AS KEY : Tuple, SET"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}