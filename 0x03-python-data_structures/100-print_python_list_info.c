#include "/usr/include/python3.4m/Python.h"
#include "/usr/include/python3.4m/object.h"
/**
 * print_python_list_info - hi!
 * @PyObject - pointer to a PyObject
 **/

/**
 * NOTES
 * from object.h:
 * line 105 = typedef of PyObject
**/

void print_python_list_info(PyObject *p);

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0;

	printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
	/* printf("[*] Allocated = %d", YYYYY); */
	
	/* for (i = 0; i < PyList_Size(p); i++) */
	for (i = 0; i == 0 && i < PyList_Size(p); i++)

	{
	/*	printf("Element %u: %s\n", PyList_GetItem(p, i), (p)->tp_name); */
	/*	printf("Element %ld", PyNumber_AsSsize_t(PyList_GetItem(p, i))); */
		/* printf("dud %s", p->tp_name); */
		printf("Element %ld", PyNumber_AsSsize_t(p, NULL));
	}
}
