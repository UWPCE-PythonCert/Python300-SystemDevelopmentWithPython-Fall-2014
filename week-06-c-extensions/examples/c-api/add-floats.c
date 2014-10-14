#include <Python.h>

static PyObject *
add(PyObject *self, PyObject *args)
{
    float x;
    float y;
    float return_value;

    if (!PyArg_ParseTuple(args, "ff", &x, &y))
        return NULL;
    return_value = x+y;
    return Py_BuildValue("f", return_value);
}

// Module's method table and initialization function
// See: http://docs.python.org/extending/extending.html#the-module-s-method-table-and-initialization-function
static PyMethodDef AddMethods[] = {
    {"add", add, METH_VARARGS, "add two numbers"},
    {NULL, NULL, 0, NULL}
};

void initadd(void) {
    // Module's initialization function
    // Will be called again if you use Python's reload()

    PyImport_AddModule("add");
    Py_InitModule("add", AddMethods);
}

int main(int argc, char *argv[]) {
    Py_SetProgramName(argv[0]);

    Py_Initialize();

    initadd();

    return 0;
}
