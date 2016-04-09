#-------------------------------------------------
#
# Project created by QtCreator 2016-02-05T14:54:06
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = testing_image
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    secdialog.cpp \
    thirddialog.cpp \
    fourthdialog.cpp \
    fifdialog.cpp \
    monidialog.cpp

HEADERS  += mainwindow.h \
    secdialog.h \
    thirddialog.h \
    fourthdialog.h \
    fifdialog.h \
    monidialog.h

FORMS    += \
    secdialog.ui \
    fifdialog.ui \
    monidialog.ui \
    teladeinicio.ui \
    manual_to_time.ui \
    time_to_pot.ui
