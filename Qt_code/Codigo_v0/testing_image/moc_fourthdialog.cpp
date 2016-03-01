/****************************************************************************
** Meta object code from reading C++ file 'fourthdialog.h'
**
** Created: Mon Feb 15 20:24:49 2016
**      by: The Qt Meta Object Compiler version 63 (Qt 4.8.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "fourthdialog.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'fourthdialog.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_fourthDialog[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       4,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      13,   34,   34,   34, 0x08,
      35,   34,   34,   34, 0x08,
      57,   34,   34,   34, 0x08,
      78,   34,   34,   34, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_fourthDialog[] = {
    "fourthDialog\0button_Plus_click3()\0\0"
    "button_Minus_click3()\0button_Plus_click4()\0"
    "button_Minus_click4()\0"
};

void fourthDialog::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        fourthDialog *_t = static_cast<fourthDialog *>(_o);
        switch (_id) {
        case 0: _t->button_Plus_click3(); break;
        case 1: _t->button_Minus_click3(); break;
        case 2: _t->button_Plus_click4(); break;
        case 3: _t->button_Minus_click4(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData fourthDialog::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject fourthDialog::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_fourthDialog,
      qt_meta_data_fourthDialog, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &fourthDialog::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *fourthDialog::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *fourthDialog::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_fourthDialog))
        return static_cast<void*>(const_cast< fourthDialog*>(this));
    return QDialog::qt_metacast(_clname);
}

int fourthDialog::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
