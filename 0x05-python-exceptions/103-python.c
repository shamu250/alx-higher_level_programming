#include <Python.h>
#include <floatobject.h>

/**
 * print_python_bytes - prints info about Python bytes objects
 * @p: PyObject
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str ? str : "(no data)");

    printf("  first %ld bytes: ", size < 10 ? size : 10);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", (unsigned char)str[i]);
        if (i + 1 < size && i + 1 < 10)
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_list - prints info about Python list objects
 * @p: PyObject
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");

    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
        else if (PyList_Check(item))
            print_python_list(item);
        else if (PyTuple_Check(item))
            printf("tuple\n");
        else if (PyLong_Check(item))
            printf("int\n");
        else if (PyUnicode_Check(item))
            printf("str\n");
        else
            printf("unknown\n");
    }
}

/**
 * print_python_float - prints info about Python float objects
 * @p: PyObject
 */
void print_python_float(PyObject *p) {
    double value;

    printf("[.] float object info\n");

    if (!PyFloat_Check(p)) {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = ((PyFloatObject *)p)->ob_fval;
    printf("  value: %f\n", value);
}
