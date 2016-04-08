#include "mainwindow.h"
#include <QApplication>
#include <QDebug>
#include <QTextStream>
#include <QtCore/QString>
#include <QtCore/QFile>
#include <QtCore/QTextStream>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();
   // QString filename = "/home/pi/Desktop/potencia.txt";
   // QFile file(filename);
   // if (file.open(QIODevice::ReadWrite)) {
     //   QTextStream stream(&file);
       // stream << "0" << endl;
         //   }
   // file.close();
//    fourthDialog temp;
////for(;;)
////    qDebug()<<temp.counter3;

     return a.exec();
}
