#include <Python.h>
/**
 * print_python_list - prints info about Python lists
 * @p: Python object (list)
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		PyObject *item;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (Py_ssize_t i = 0; i < size; i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
	else
	{
		printf("[*] Python list info\n");
		printf("	[ERROR] Invalid List Object\n");
	}
}
/**
 * print_python_bytes - prints info about Python bytes objects
 * @p: Python object (bytes)
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("	size: %ld\n", PyBytes_Size(p));
		printf("	trying string: %s\n", PyBytes_AsString(p));
		printf("[.] first 10 bytes: ");

		Py_ssize_t size = PyBytes_Size(p);
		Py_ssize_t max_print = (size < 10) ? size : 10;

		for (Py_ssize_t i = 0; i < max_print; i++)
		{
			printf("%02hhx", ((unsigned char *)PyBytes_AsString(p))[i]);
			if (i < max_print - 1)
			{
				printf(" ");
			}
		}
		printf("\n");
	}
	else
	{
		printf("[.] bytes object info\n");
		printf("	[ERROR] Invalid Bytes Object\n");
	}
}
