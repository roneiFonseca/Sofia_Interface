/****************************************************************************
** Meta object code from reading C++ file 'monidialog.h'
**
** Created: Mon Feb 15 22:08:57 2016
**      by: The Qt Meta Object Compiler version 63 (Qt 4.8.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "monidialog.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'monidialog.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_moniDialog[] = {

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
      11,   35,   35,   35, 0x08,
      36,   35,   35,   35, 0x08,
      64,   35,   35,   35, 0x08,
      87,   35,   35,   35, 0x08,
     112,   35,   35,   35, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_moniDialog[] = {
    "moniDialog\0updateLCD_temp(QString)\0\0"
    "updateLCD_potencia(QString)\0"
    "updateLCD_imp(QString)\0updateLCD_tempo(QString)\0"
    "on_pushButton_8_clicked()\0"
};

void moniDialog::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        moniDialog *_t = static_cast<moniDialog *>(_o);
        switch (_id) {
        case 0: _t->updateLCD_temp((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 1: _t->updateLCD_potencia((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 2: _t->updateLCD_imp((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 3: _t->updateLCD_tempo((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 4: _t->on_pushButton_8_clicked(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData moniDialog::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject moniDialog::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_moniDialog,
      qt_meta_data_moniDialog, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &moniDialog::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *moniDialog::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *moniDialog::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_moniDialog))
        return static_cast<void*>(const_cast< moniDialog*>(this));
    return QDialog::qt_metacast(_clname);
}

int moniDialog::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
