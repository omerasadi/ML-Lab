{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "799f068f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['a', 'b', 'c'], dtype='<U1')"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "char_arr = np.array(['a','b','c'])\n",
    "char_arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e80cd33e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['supervised', 'unsupervised', 'semi-supervised', 'reinforcement'],\n",
       "      dtype='<U15')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ch_arr2 = np.array([\"supervised\",\"unsupervised\",\"sEMi-supervised\",\"reinforcement\"])\n",
    "low_arr = np.char.lower(ch_arr2)\n",
    "low_arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cdde0824",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['supervised', 'unsupervised', 'semi supervised', 'reinforcement'],\n",
       "      dtype='<U15')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cleaned_arr = np.char.replace(low_arr,\"-\",\" \")\n",
    "cleaned_arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "674374a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int32')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array1=np.array([1,2,3])\n",
    "array1.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "56e04798",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('<U15')"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "low_arr.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "960f01e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "array8=np.array([1,2,3,4],dtype='i')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6d0e3bef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4], dtype=int32)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2538061b",
   "metadata": {},
   "outputs": [],
   "source": [
    "array2conv=array8.astype('f')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "266e6909",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 0, 0],\n",
       "       [0, 0, 0],\n",
       "       [0, 0, 0]], dtype=int64)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ars0 = np.zeros((3,3),dtype=\"int64\")\n",
    "ars0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "0e253863",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.4918558 , 0.81563398, 0.58742839])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ars3= np.random.random(3)\n",
    "ars3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "59e4eb92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dimones=np.ones((4,3,2))\n",
    "dimones\n",
    "dimones.ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "1f007009",
   "metadata": {},
   "outputs": [],
   "source": [
    "ar1=np.array([1,2,3])\n",
    "ar2=np.array([2,4,6])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d40cfa1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "power=np.power(ar1,ar2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "befeecc3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[11, 22, 25],\n",
       "       [14, 25, 28]])"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array2d = np.array([[1,2,3],[4,5,6]])\n",
    "array1d=np.array([10,20,22])\n",
    "result=array2d+array1d\n",
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "a06a3d4e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 3, 6, 9])"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "range_arr= np.arange(0,10,3)\n",
    "range_arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "480d98ef",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
