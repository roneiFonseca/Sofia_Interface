/****************************************************************************
** Meta object code from reading C++ file 'thirddialog.h'
**
** Created: Tue Feb 16 12:25:29 2016
**      by: The Qt Meta Object Compiler version 63 (Qt 4.8.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "thirddialog.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'thirddialog.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_thirdDialog[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      12,   32,   32,   32, 0x08,
      33,   32,   32,   32, 0x08,
      54,   32,   32,   32, 0x08,
      75,   32,   32,   32, 0x08,
      97,   32,   32,   32, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_thirdDialog[] = {
    "thirdDialog\0button_Plus_click()\0\0"
    "button_Minus_click()\0button_Plus_click2()\0"
    "button_Minus_click2()\0on_pushButton_5_clicked()\0"
};

void thirdDialog::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        thirdDialog *_t = static_cast<thirdDialog *>(_o);
        switch (_id) {
        case 0: _t->button_Plus_click(); break;
        case 1: _t->button_Minus_click(); break;
        case 2: _t->button_Plus_click2(); break;
        case 3: _t->button_Minus_click2(); break;
        case 4: _t->on_pushButton_5_clicked(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData thirdDialog::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject thirdDialog::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_thirdDialog,
      qt_meta_data_thirdDialog, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &thirdDialog::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *thirdDialog::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *thirdDialog::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_thirdDialog))
        return static_cast<void*>(const_cast< thirdDialog*>(this));
    return QDialog::qt_metacast(_clname);
}

int thirdDialog::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
