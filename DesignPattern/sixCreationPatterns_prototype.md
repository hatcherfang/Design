## [六个创建型模式-factory pattern](http://blog.csdn.net/lovelion/article/details/17517213)  
### [原型模式-Prototype Pattern【学习难度：★★★☆☆，使用频率：★★★☆☆】](http://blog.csdn.net/lovelion/article/details/7424559)  
张纪中版《西游记》以出乎意料的造型和雷人的台词遭到广大观众朋友的热议，我们在此对该话题不作过多讨论。但无论是哪个版本的《西游记》，孙悟空都是其中的一号雄性主角，关于他（或它）拔毛变小猴的故事几乎人人皆知，孙悟空可以用猴毛根据自己的形象，复制（又称“克隆”或“拷贝”）出很多跟自己长得一模一样的“身外身”来。在设计模式中也存在一个类似的模式，可以通过一个原型对象克隆出多个一模一样的对象，该模式称之为原型模式。  
1. 大同小异的工作周报   
> Sunny软件公司一直使用自行开发的一套OA (Office Automatic，办公自动化)系统进行日常工作办理，但在使用过程中，越来越多的人对工作周报的创建和编写模块产生了抱怨。追其原因，Sunny软件公司的OA管理员发现，由于某些岗位每周工作存在重复性，工作周报内容都大同小异，如图7-1工作周报示意图。这些周报只有一些小地方存在差异，但是现行系统每周默认创建的周报都是空白报表，用户只能通过重新输入或不断复制粘贴来填写重复的周报内容，极大降低了工作效率，浪费宝贵的时间。如何快速创建相同或者相似的工作周报，成为Sunny公司OA开发人员面临的一个新问题。  

> Sunny公司的开发人员通过对问题进行仔细分析，决定按照如下思路对工作周报模块进行重新设计和实现：  
  (1)除了允许用户创建新周报外，还允许用户将创建好的周报保存为模板；  
  (2)用户在再次创建周报时，可以创建全新的周报，还可以选择合适的模板复制生成一份相同的周报，然后对新生成的周报根据实际情况进行修改，产生新的周报。  
  只要按照如上两个步骤进行处理，工作周报的创建效率将得以大大提高。这个过程让我们想到平时经常进行的两个电脑基本操作：复制和粘贴，快捷键通常为Ctrl + C和Ctrl + V，通过对已有对象的复制和粘贴，我们可以创建大量的相同对象。如何在一个面向对象系统中实现对象的复制和粘贴呢？不用着急，本章我们介绍的原型模式正为解决此类问题而诞生。  

2. 原型模式概述  
在使用原型模式时，我们需要首先创建一个原型对象，再通过复制这个原型对象来创建更多同类型的对象。试想，如果连孙悟空的模样都不知道，怎么拔毛变小猴子呢？原型模式的定义如下：  
```
原型模式(Prototype  Pattern)：使用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
原型模式是一种对象创建型模式。  
```
原型模式的工作原理很简单：将一个原型对象传给那个要发动创建的对象，这个要发动创建的对象通过请求原型对象拷贝自己来实现创建过程。由于在软件系统中我们经常会遇到需要创建多个相同或者相似对象的情况，因此原型模式在真实开发中的使用频率还是非常高的。原型模式是一种“另类”的创建型模式，创建克隆对象的工厂就是原型类自身，工厂方法由克隆方法来实现。  
  需要注意的是通过克隆方法所创建的对象是全新的对象，它们在内存中拥有新的地址，通常对克隆所产生的对象进行修改对原型对象不会造成任何影响，每一个克隆对象都是相互独立的。通过不同的方式修改可以得到一系列相似但不完全相同的对象。  
原型模式的结构如图7-2所示：  
<div align="center">
<img src=https://github.com/hatcherfang/Design/blob/master/DesignPattern/images/prototypePattern-2.gif alt="图7-2 原型模式结构图">  
<br>
图7-2 原型模式结构图
</div>  

在原型模式结构图中包含如下几个角色：  
  ●Prototype（抽象原型类）：它是声明克隆方法的接口，是所有具体原型类的公共父类，可以是抽象类也可以是接口，甚至还可以是具体实现类。  
  ● ConcretePrototype（具体原型类）：它实现在抽象原型类中声明的克隆方法，在克隆方法中返回自己的一个克隆对象。  
  ● Client（客户类）：让一个原型对象克隆自身从而创建一个新的对象，在客户类中只需要直接实例化或通过工厂方法等方式创建一个原型对象，再通过调用该对象的克隆方法即可得到多个相同的对象。由于客户类针对抽象原型类Prototype编程，因此用户可以根据需要选择具体原型类，系统具有较好的可扩展性，增加或更换具体原型类都很方便。  
原型模式的核心在于如何实现克隆方法，下面将介绍两种在Java语言中常用的克隆实现方法：  
2.1 通用实现方法  
通用的克隆实现方法是在具体原型类的克隆方法中实例化一个与自身类型相同的对象并将其返回，并将相关的参数传入新创建的对象中，保证它们的成员属性相同。示意代码如下所示：  

```
class ConcretePrototype implements Prototype
{
  private String  attr; //成员属性
  public void  setAttr(String attr)
  {
      this.attr = attr;
  
  }
  public String  getAttr()
  {
      return this.attr;
  
  }
  public Prototype  clone() //克隆方法
  {
      Prototype  prototype = new ConcretePrototype(); //创建新对象
      prototype.setAttr(this.attr);
      return prototype;
  
  }
}
```
在客户类中我们只需要创建一个ConcretePrototype对象作为原型对象，然后调用其clone()方法即可得到对应的克隆对象，如下代码所示：  
Prototype obj1 = new ConcretePrototype();  
obj1.setAttr("Sunny");  
Prototype obj2  = obj1.clone();  
这种方法可作为原型模式的通用实现，它与编程语言特性无关，任何面向对象语言都可以使用这种形式来实现对原型的克隆。  
2.2 Java语言提供的clone()方法  
  学过Java语言的人都知道，所有的Java类都继承自java.lang.Object。事实上，Object类提供一个clone()方法，可以将一个Java对象复制一份。因此在Java中可以直接使用Object提供的clone()方法来实现对象的克隆，Java语言中的原型模式实现很简单。  
  需要注意的是能够实现克隆的Java类必须实现一个标识接口Cloneable，表示这个Java类支持被复制。如果一个类没有实现这个接口但是调用了clone()方法，Java编译器将抛出一个CloneNotSupportedException异常。如下代码所示：  
```
class ConcretePrototype implements  Cloneable
{
  ……
  public Prototype  clone()
  {
  　　Object object = null;
  　　try {
  　　　　　object = super.clone();
  　　
  } catch (CloneNotSupportedException exception) {
  　　　　　System.err.println("Not support cloneable");
  　　
  }
  　　return (Prototype )object;
  
  }
  ……

}
```
  在客户端创建原型对象和克隆对象也很简单，如下代码所示：  
Prototype obj1  = new ConcretePrototype();  
Prototype obj2  = obj1.clone();  
  一般而言，Java语言中的clone()方法满足：  
(1) 对任何对象x，都有x.clone() != x，即克隆对象与原型对象不是同一个对象；  
(2) 对任何对象x，都有x.clone().getClass() == x.getClass()，即克隆对象与原型对象的类型一样；  
(3) 如果对象x的equals()方法定义恰当，那么x.clone().equals(x)应该成立。  
  为了获取对象的一份拷贝，我们可以直接利用Object类的clone()方法，具体步骤如下：  
(1) 在派生类中覆盖基类的clone()方法，并声明为public；  
(2) 在派生类的clone()方法中，调用super.clone()；  
(3)派生类需实现Cloneable接口。  
  此时，Object类相当于抽象原型类，所有实现了Cloneable接口的类相当于具体原型类。  
### [对象的克隆——原型模式（二）](http://blog.csdn.net/lovelion/article/details/7424594)  
1. 完整解决方案  
Sunny公司开发人员决定使用原型模式来实现工作周报的快速创建，快速创建工作周报结构图如图7-3所示：  
<div align="center">  
<img src=https://github.com/hatcherfang/Design/blob/master/DesignPattern/images/quickCreateWorkWeekReport-3.gif alt="图7-3 快速创建工作周报结构图">  
<br>
图7-3 快速创建工作周报结构图  
</div>  

在图7-3中，WeeklyLog充当具体原型类，Object类充当抽象原型类，clone()方法为原型方法。WeeklyLog类的代码如下所示：  
```
//工作周报WeeklyLog：具体原型类，考虑到代码的可读性和易理解性，只列出部分与模式相关的核心代码  
class WeeklyLog implements Cloneable
{
       private  String name;
       private  String date;
       private  String content;
       public  void setName(String name) {
              this.name  = name;
       
       }
       public  void setDate(String date) {
              this.date  = date;
       
       }
       public  void setContent(String content) {
              this.content  = content;
       
       }
       public  String getName() {
              return  (this.name);
       
       }
       public  String getDate() {
              return  (this.date);
       
       }
       public  String getContent() {
              return  (this.content);
       
       }
     //克隆方法clone()，此处使用Java语言提供的克隆机制
       public WeeklyLog clone()
       {
              Object obj = null;
              try
	      {
                     obj = super.clone();
                     return (WeeklyLog)obj;     
              
	}
              catch(CloneNotSupportedException e)
	      {
                     System.out.println("不支持复制！");
                     return null;
              
	}
       
       }

}
```
编写如下客户端测试代码：  
```
class Client
{
       public  static void main(String args[])
       {
              WeeklyLog log_previous = new WeeklyLog();  //创建原型对象
              log_previous.setName("张无忌");
              log_previous.setDate("第12周");
              log_previous.setContent("这周工作很忙，每天加班！");
             
              System.out.println("****周报****");
              System.out.println("周次：" +  log_previous.getDate());
              System.out.println("姓名：" +  log_previous.getName());
              System.out.println("内容：" +  log_previous.getContent());
              System.out.println("--------------------------------");
             
              WeeklyLog  log_new;
              log_new  = log_previous.clone(); //调用克隆方法创建克隆对象
              log_new.setDate("第13周");
              System.out.println("****周报****");
              System.out.println("周次：" + log_new.getDate());
              System.out.println("姓名：" + log_new.getName());
              System.out.println("内容：" + log_new.getContent());
       
       }

}
```
编译并运行程序，输出结果如下：  
```
****周报****
周次：第12周
姓名：张无忌
内容：这周工作很忙，每天加班！
--------------------------------
****周报****
周次：第13周
姓名：张无忌
内容：这周工作很忙，每天加班！
```
通过已创建的工作周报可以快速创建新的周报，然后再根据需要修改周报，无须再从头开始创建。原型模式为工作流系统中任务单的快速生成提供了一种解决方案。  
### [对象的克隆——原型模式（三）](http://blog.csdn.net/lovelion/article/details/7424620)  
1. 带附件的周报  
通过引入原型模式，Sunny软件公司OA系统支持工作周报的快速克隆，极大提高了工作周报的编写效率，受到员工的一致好评。但有员工又发现一个问题，有些工作周报带有附件，例如经理助理“小龙女”的周报通常附有本周项目进展报告汇总表、本周客户反馈信息汇总表等，如果使用上述原型模式来复制周报，周报虽然可以复制，但是周报的附件并不能复制，这是由于什么原因导致的呢？如何才能实现周报和附件的同时复制呢？我们在本节将讨论如何解决这些问题。  
  在回答这些问题之前，先介绍一下两种不同的克隆方法，浅克隆(ShallowClone)和深克隆(DeepClone)。在Java语言中，数据类型分为值类型（基本数据类型）和引用类型，值类型包括int、double、byte、boolean、char等简单数据类型，引用类型包括类、接口、数组等复杂类型。浅克隆和深克隆的主要区别在于是否支持引用类型的成员变量的复制，下面将对两者进行详细介绍。  
1.1 浅克隆  
  在浅克隆中，如果原型对象的成员变量是值类型，将复制一份给克隆对象；如果原型对象的成员变量是引用类型，则将引用对象的地址复制一份给克隆对象，也就是说原型对象和克隆对象的成员变量指向相同的内存地址。简单来说，在浅克隆中，当对象被复制时只复制它本身和其中包含的值类型的成员变量，而引用类型的成员对象并没有复制，如图7-4所示(略)  

