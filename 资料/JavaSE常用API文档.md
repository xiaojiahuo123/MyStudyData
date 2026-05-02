# 一、java.lang.Object类

## 1.1 Object根父类

Object 是类层次结构的根类。每个类都使用 Object 作为超类。所有对象（包括数组）都实现这个类的方法。

特别说明：String[]对象数组是Object[]子类，而int[]不是Object[]子类，它们都是Object的子类。

![image-20230823182748086](JavaSE常用API文档.assets/image-20230823182748086.png)

## 1.2 Object类的方法

- **public String toString()**：建议实体Javabean重写，重写快捷键Alt+Insert。在Object类中默认返回对象的运行时类型@对象的hashCode十六进制值。
- **public final native Class<?> getClass()**：返回当前对象的运行时类型。
- **public native int hashCode()**：返回当前对象的hash值。
- **public boolean equals(Object obj)**：比较当前对象与指定对象obj是否相等。在Object类中默认比较地址值（等价于==）。equals和hashCode方法要一起重写，重写快捷键Alt+Insert。
- **protected native Object clone() throws CloneNotSupportedException**：克隆当前对象。子类如果要在子类外部使用克隆功能，必须实现java.lang.Cloneable接口，并重写该方法。
- **protected void finalize() throws Throwable**：当当前对象被GC回收时，自动由GC调用。该方法从JDK9之后已被废弃。
- **public final native void wait(long timeoutMillis) throws InterruptedException**
- **public final void wait(long timeoutMillis, int nanos) throws InterruptedException**：当前对象作为同步锁对象，执行该方法，使得当前线程进入阻塞状态，并是否同步锁对象和CPU资源。直到时间到，或当前线程被其他唤醒。
- **public final void wait() throws InterruptedException**：当前对象作为同步锁对象，执行该方法，使得当前线程进入阻塞状态，并是否同步锁对象和CPU资源。直到当前线程被其他唤醒。
- **public final native void notify()**：唤醒其中一个等待被唤醒的线程，而且只能唤醒以当前对象为同步锁对象的等待线程。
- **public final native void notifyAll()**：唤醒所有等待被唤醒的线程，并且这些线程也以当前对象为同步锁对象。
- 上述wait、notify、notifyAll的5个方法必须由同步锁对象调用。

## 1.3 java.lang.Cloneable接口

该接口是一个标识型接口，不包含抽象方法。当一个类的对象需要支持克隆操作时，实现该接口，并重写Object类的clone方法即可。



# 二、Java的包装类

## 2.1 Java的包装类型



|      | 基本数据类型 | 包装类（java.lang包） | 缓存共享的常量对象 |
| ---- | ------------ | --------------------- | ------------------ |
| 1    | byte         | Byte                  | [-128,127]         |
| 2    | short        | Short                 | [-128,127]         |
| 3    | int          | Integer               | [-128,127]         |
| 4    | long         | Long                  | [-128,127]         |
| 5    | float        | Float                 | 无                 |
| 6    | double       | Double                | 无                 |
| 7    | char         | Character             | [0,127]            |
| 8    | boolean      | Boolean               | true,false         |

•包装类对象不可变，部分包装类有缓存对象

•包装类与对应基本数据类型之间支持自动装箱与自动拆箱

•两个包装类对象进行==和!=比较是直接比较地址值，遇到其他运算符拆箱为基本数据类型值计算

•一个包装类对象与一个基本数据类型值使用运算符计算，都会将包装类拆箱为基本数据类型值计算

## 2.2 包装类的相关方法

### 1、获取包装类对象

- public static Integer valueOf(int i)：获取Integer对象

- public static Integer valueOf(String s) throws NumberFormatException：将字符串转为Integer对象


其他包装类类似，从JDK9开始，包装类的构造器被废弃了

### 2、将字符串转为基本数据类型值

- public static int parseInt(String s) throws NumberFormatException：将字符串的整数值转为int型整数值

- public static double parseDouble(String s) throws NumberFormatException：将字符串类型的小数值转为double型的小数值

- public static boolean parseBoolean(String s)：将字符串类型的true或false转为boolean类型的布尔值


- 除Character外，7种包装类都有上述对应方法


- public char charAt(int index)：将字符串中的[index]位置的字符取出来


### 3、获取某种数据类型最大值、最小值

- Integer.MAX_VALUE：int最大值

- Integer.MIN_VALUE：int最小值

- 除Boolean外， 7种包装类都有上述常量值


### 4、比较相等

- boolean equals(Object obj)：包装类都重写了Object类的equals方法，比较两个包装类对象的值


### 5、比较大小

- Integer类 public static int compare(int x, int y)：比较两个int值大小关系。x>y返回正整数，x=y返回0，x<y返回负整数。

- Double类 public static int compare(double x, double y)：比较两个double值大小关系。x>y返回正整数，x=y返回0，x<y返回负整数。

- 8种包装类都有对应的compare方法。

### 6、转进制（以Integer为例）

- public static String toBinaryString(int i)：将十进制int值转为二进制

- public static String toOctalString(int i) ：将十进制int值转为八进制

- public static String toHexString(int i) ：将十进制int值转为十六进制


### 7、字符处理和判断（Character类）

- public static char toLowerCase(char ch)：转为小写字母

- public static char toUpperCase(char ch)：转为大写字母

- public static boolean isDigit(char ch)：ch字符是不是一个数字字符

- public static boolean isLetter(char ch)：ch字符是不是一个字母

- public static boolean isLetterOrDigit(char ch)：ch字符是不是一个数字字符或字母

- public static boolean isWhitespace(char ch)：ch字符是不是一个空白字符


# 三、数学计算工具类

## 3.1 相关的类

- java.lang.Math类：包含用于执行基本数学运算的方法，如随机值、绝对值、最大最小值、平方根、初等指数、对数和三角函数等，还包含圆周率PI、自然对数的底数E等。

- java.math.BigInteger：用于表示不可变的任何精度的整数。

- java.math.BigDecimal：用于表示不可变的任意精度的小数。

- java.util.Random：用于产生各种基本数据类型的伪随机值。


## 3.2 java.lang.Math类

public static final double E：自然底数

public static final double PI：圆周率

public static double random()：随机产生并返回[0,1)范围的double值。

public static double abs(double a)：求绝对值。支持int、long、float、double四种重载形式。

public static double max(double a, double b)：求a,b的最大值。支持int、long、float、double四种重载形式。

public static double min(double a, double b) ：求a,b的最小值。支持int、long、float、double四种重载形式。

public static double floor(double a) ：对a进行向下取整。

public static double ceil(double a)：对a进行向上取整。

public static long round(double a)：对a进行四舍五入。 相当于(int)(a+0.5)。

public static double sqrt(double a)：求a的平方根值。

public static double cbrt(double a)：求a的立方根值。

public static double pow(double a, double b)：求![image-20230823183932930](JavaSE常用API文档.assets/image-20230823183932930.png)。

public static double exp(double a)：求![image-20230823183950295](JavaSE常用API文档.assets/image-20230823183950295.png)。

public static double log(double a)：求![image-20230823184137151](JavaSE常用API文档.assets/image-20230823184137151.png)。

public static double log10(double a)：求![image-20230823184517903](JavaSE常用API文档.assets/image-20230823184517903.png)。

还有sin,cos,tan,asin,acos,atan等三角函数。


## 3.3 java.math.BigInteger类

- public BigInteger(String val)：创建BigInteger对象。

- public BigInteger abs()：求绝对值

- public BigInteger add(BigInteger val)：求this与val的和，即 this + val。

- public BigInteger subtract(BigInteger val)：求this与val的差，即this - val。

- public BigInteger multiply(BigInteger val)：求this与val的乘积，即this × val。

- public BigInteger divide(BigInteger val)：求this与val的商，即this ÷ val。

- public BigInteger remainder(BigInteger val)：求this与val的余数，即this % val。

- public BigInteger[] divideAndRemainder(BigInteger val)：求this与val的商和余数。

- public BigInteger pow(int exponent)：求this的exponent幂次方。

- public BigInteger max(BigInteger val)：求this和val的最大值。

- public BigInteger min(BigInteger val)：求this和val的最小值。


## 3.4 java.math.BigDecimal类

- public BigDecimal(String val)：创建BigDecimal对象。

- public BigDecimal abs()：求绝对值

- public BigDecimal add(BigDecimal val)：求this与val的和，即 this + val。

- public BigDecimal subtract(BigDecimal val)：求this与val的差，即this - val。

- public BigDecimal multiply(BigDecimal val)：求this与val的乘积，即this × val。

- public BigDecimal divide(BigDecimal val)：求this与val的商，即this ÷ val，要求能除尽。

- public BigDecimal divide(BigDecimal divisor, int scale, RoundingMode roundingMode)：求this与divisor的商，结果保留scale位小数，对于第scale+1位出来方式由roundingMode指定的舍入模式决定。

- public BigDecimal remainder(BigDecimal val)：求this与val的余数，即this % val。

- public BigDecimal pow(int n)：求this的n幂次方。

- public BigDecimal max(BigInteger val)：求this和val的最大值。

- public BigDecimal min(BigInteger val)：求this和val的最小值。


## 3.5 java.util.Random类

- public Random() ：默认使用系统时间作为随机种子，创建Random 对象。

- public Random(long seed) ：指定随机种子，创建Random 对象。随机种子相同的两个Random()对象，将生成并返回相同的数字序列。

- public boolean nextBoolean() ：随机产生1个boolean值。

- public double nextDouble() ：随机产生1个[0,1)的double值。

- public float nextFloat() ：随机产生1个[0,1)的float值。

- public int nextInt() ： 随机产生1个int值。

- public int nextInt(int n) ：随机产生1个[0,n)范围的int值。

- public long nextLong()：随机产生1个long值。

- public void nextBytes(byte[] bytes) ：随机产生一组byte值，放到bytes数组中。


# 四、系统工具类

## 4.1 java.lang.System类

在 System 类提供的设施中，有标准输入、标准输出和错误输出流；对外部定义的属性和环境变量的访问；加载文件和库的方法；还有快速复制数组的一部分的实用方法。

- public static final InputStream in：“标准”输入流。此流已打开并准备提供输入数据。通常，此流对应于键盘输入或者由主机环境或用户指定的另一个输入源。

- public static final PrintStream out：“标准”输出流。此流已打开并准备接受输出数据。通常，此流对应于显示器输出或者由主机环境或用户指定的另一个输出目标。

- public static final PrintStream err：“标准”错误输出流。此流已打开并准备接受输出数据。按照惯例，此输出流用于显示错误消息。

- public static void setIn(InputStream in)：重新分配“标准”输入流。 

- public static void setOut(PrintStream out)：重新分配“标准”输出流。

- public static void setErr(PrintStream err)：重新分配“标准”错误输出流。

- public static Properties getProperties()：确定当前的系统属性。

- public static void setProperties(Properties props)：将系统属性设置为 Properties 参数。 

- public static String getProperty(String key)：获取指定键指示的系统属性。

- public static String setProperty(String key,String value)：设置指定键指示的系统属性。

- public static String clearProperty(String key)：移除指定键指示的系统属性。


![image-20230823184943465](JavaSE常用API文档.assets/image-20230823184943465.png)

- public static long currentTimeMillis()：返回以毫秒为单位的当前时间。当前时间与协调世界时 1970 年 1 月 1 日午夜之间的时间差（以毫秒为单位测量）。

- public static void exit(int status)：终止当前正在运行的 Java 虚拟机。参数用作状态码；根据惯例，非 0 的状态码表示异常终止。 

- public static void gc()：运行垃圾回收器。 

- public static native void arraycopy(Object src,  int srcPos, Object dest, int destPos, int length)：从指定源数组src中复制length个元素到一个目标数组dest ， 将src数组的[srcPos, srcPos+length)元素复制到dest数组的[destPos, destPos+length)。


## 4.2 java.lang.Runtime类

每个 Java 应用程序都有唯一的一个 Runtime 类实例，使应用程序能够与其运行的环境相连接。可以通过 getRuntime 方法获取当前运行时类的实例对象。

- public static Runtime getRuntime()：返回与当前 Java 应用程序相关的运行时对象。

- public native long totalMemory()：返回 Java 虚拟机中的内存总量。

- public native long maxMemory()：返回 Java 虚拟机试图使用的最大内存量。

- public native long freeMemory()：返回 Java 虚拟机中的空闲内存量。

- public void exit(int status)：终止当前正在运行的 Java 虚拟机。参数用作状态码；根据惯例，非 0 的状态码表示异常终止。 System.exit 方法是调用此方法的一种传统而便捷的方式。

- public void gc()：运行垃圾回收器。方法 System.gc() 是调用此方法的一种传统而便捷的方式。


# 五、日期时间工具类

## 5.1 日期时间工具类

Java核心类库中提高了3代日期时间API：

### 第1代

- java.util.Date类：表示特定的瞬间，精确到毫秒。

- 
  java.text.SimpleDateFormat类：一个以与语言环境有关的方式来格式化和解析日期的具体类。它允许进行格式化（日期 -> 文本）、解析（文本 -> 日期）。


### 第2代

- java.util.Calendar类：是一个抽象类，它为特定瞬间与一组诸如 YEAR、MONTH、DAY_OF_MONTH、HOUR 等 日历字段之间的转换提供了一些方法，并为操作日历字段（例如获得下星期的日期）提供了一些方法。

- java.util.Locale类：表示了特定的地理、政治和文化地区。例如：Locale.CHINA

- java.util.TimeZone类：表示时区偏移量，也可以计算夏令时。例如： TimeZone.getTimeZone(“America/Los_Angeles”) 或 TimeZone. getDefault()。


### 第3代

- java.time.Instant类：在时间线上的瞬间点。这可能用于在应用程序中记录事件时间戳。类似于第1代的Date类。

- java.time.LocalDate / java.time.LocalTime / java.time.LocalDateTime类：本地日期 / 本地时间 / 本地日期时间

- java.time.ZoneId类：一个时区ID，如Europe/Paris。

- java.time.ZoneOffset类：与格林威治/ UTC的时区偏移量，如+02:00。

- java.time.ZonedDateTime类：具有时区的日期时间。

- java.time.Period类： ISO-8601日历系统中的日期时间，例如“2年3个月4天”。 

- java.time.Duration类：基于时间的时间量，如'34.5秒'。

- java.time.Year / java.time.Month / java.time.YearMonth / java.time.MonthDay / java.time.DayOfWeek 类：年份 / 月份 / 年份月份 / 月份日期 / 星期

- java.time.format.DateTimeFormatter类：用于打印和解析日期时间对象。 类似于第1代的SimpleDateFormat类。


## 5.2 第1代

### 5.2.1 java.util.Date类

- public Date()：获取当前系统时间，精确到毫秒。

- public Date(long date)：获取距离1970 年 1 月 1 日 00:00:00 GMT以来经过date毫秒数的系统时间。

- public long getTime()：返回自 1970 年 1 月 1 日 00:00:00 GMT 以来此 Date 对象表示的毫秒数。

- public String toString()：把此 Date 对象转换为以下形式的字符串： week mon dd hh:mm:ss zzz yyyy 其中： dow 是一周中的某一天 (Sun, Mon, Tue, Wed, Thu, Fri, Sat)。


==第1代与第三代的转换：==

- public Instant toInstant()：将此Date对象转换为Instant。

- public static Date from(Instant instant)：将Instant对象转为Date对象。




### 5.2.2 java.text.SimpleDateFormat类

- public SimpleDateFormat(String pattern):用给定的模式和默认语言环境的日期格式符号构造 SimpleDateFormat。

- public final String format(Date date)：将一个 Date 格式化为日期/时间字符串。

- public Date parse(String source)throws ParseException：从给定字符串的开始解析文本，以生成一个日期。


![image-20230823192157142](JavaSE常用API文档.assets/image-20230823192157142.png)

## 5.3 第2代

### 5.3.1 java.util.Calendar类

- Calendar.YEAR / MONTH / DATE / DAY_OF_YEAR 等常量字段。

- public static Calendar getInstance()：使用默认时区和语言环境获得一个日历。

- public static Calendar getInstance(TimeZone zone,Locale aLocale)：使用指定时区和语言环境获得一个日历。

- public TimeZone getTimeZone()：获得时区。

- public void set(int field, int value) ：将给定的日历字段设置为给定值。field是Calendar类的YEAR等常量字段值。

- public int get(int field)：返回给定日历字段的值。field是Calendar类的YEAR等常量字段值。

- public long getTimeInMillis()：返回此 Calendar 的时间值，以毫秒为单位。 

- public void setTimeInMillis(long millis)：用给定的 long 毫秒值设置此 Calendar 的当前时间值。

- public final void set(int year,int month, int date)：设置日历字段 YEAR、MONTH 和 DAY_OF_MONTH 的值。保留其他日历字段以前的值。如果不需要这样做，则先调用 clear()。

- public final void set(int year,int month,int date,int hourOfDay,int minute,int second)：设置字段 YEAR、MONTH、DAY_OF_MONTH、HOUR、MINUTE 和 SECOND 的值。保留其他字段以前的值。如果不需要这样做，则先调用 clear()。

- public int getActualMaximum(int field)：给定此 Calendar 的时间值，返回指定日历字段可能拥有的最大值。例如：二月份最大值可能是28或29。


==第1代与第2代的转换：==

- public Date getTime()：返回一个表示此 Calendar 时间值的 Date 对象。

- public final void setTime(Date date)：使用给定的 Date 设置此 Calendar 的时间。


### 5.3.2 java.util.TimeZone类

- public static TimeZone getDefault()：获取此主机的默认 TimeZone。

- public static TimeZone getTimeZone(String ID)：获取给定 ID 的 TimeZone。例如 “America/Los_Angeles”，获自定义 ID（如 "GMT-8:00"）。

- public static String[] getAvailableIDs()：获取受支持的所有可用 ID。


### 5.3.3 java.util.Locale类

- Locale.CHINA 、CHINESE、 CANADA、US、ENGLISH 等常量。

- public static Locale getDefault()：获得此 Java 虚拟机实例的当前默认语言环境值。

- public Locale(String language, String country)：根据语言和国家/地区构造一个语言环境。例如zh代表中文，CN代表中国。 


## 5.4 第3代

![image-20230825191156249](JavaSE常用API文档.assets/image-20230825191156249.png)

### 5.3.1 java.time.Instant类

| 返回值  | 方法                            | **描述**                                       |
| ------- | ------------------------------- | ---------------------------------------------- |
| Instant | now()                           | 从系统时钟获取当前瞬间。本初子午线的系统时间。 |
| Instant | ofEpochMilli(long epochMilli)   | 距离1970-1-1 0:0:0过了epochMilli毫秒的系统时间 |
| Instant | ofEpochSecond(long epochSecond) | 距离1970-1-1 0:0:0过了epochSecond秒的系统时间  |

### 5.3.2 java.time.LocalDate类

| 返回值        | 方法                                                         | **描述**                                                     |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| LocalDate     | now() <br />now(ZoneId zone)                                 | 静态方法，按照平台默认的时区创建LocalDate对象<br />静态方法，按照指定时区创建LocalDate对象 |
| LocalDate     | of(int year, int month, int dayOfMonth)                      | 静态方法，根据指定日期创建LocalDate对象                      |
|               |                                                              |                                                              |
| int           | getYear()<br />getMonthValue()<br />getDayOfMonth()<br />getDayOfYear()<br />lengthOfMonth()<br />lengthOfYear() | 获取年份值<br />获得月份值(1-12)<br />获得在月份中的天数(1-31) <br />获得在年中的天数(1-366)<br />获取当月的总天数<br />获取当年的总天数 |
| Month         | getMonth()                                                   | 获取月份对象, 返回一个Month枚举值                            |
| DayOfWeek     | getDayOfWeek()                                               | 获得星期几(返回一个 DayOfWeek 枚举值)                        |
|               |                                                              |                                                              |
| LocalDate     | withYear(int year)<br />withMonth(int month)<br />withDayOfMonth(int dayOfMonth)<br />withDayOfYear(int dayOfYear)<br />with(TemporalAdjuster  t) | 更改年份值返回一个新LocalDate对象<br />更改月份值返回一个新LocalDate对象<br />更改日期值返回一个新LocalDate对象<br />更改当年第几天的值返回一个新LocalDate对象<br />更改对应的Period返回一个新LocalDate对象 |
| LocalDate     | plusYears(long years)<br />plusMonths(long minute)<br />plusWeeks(long weeks)<br />plusDays(long days)<br />plus(TemporalAmount t) | 增加几年返回新LocalDate对象<br />增加几月返回新LocalDate对象<br />增加几周返回新LocalDate对象<br />增加几日返回新LocalDate对象<br />增加一个Period返回新LocalDate对象 |
| LocalDate     | minusYears(long years)<br />minusMonths(long minute)<br />minusWeeks(long weeks)<br />minusDays(long days)<br />minus(TemporalAmount t) | 减少几年返回新LocalDate对象<br />减少几月返回新LocalDate对象<br />减少几周返回新LocalDate对象<br />减少几日返回新LocalDate对象<br />减少一个 Period返回新LocalDate对象 |
|               |                                                              |                                                              |
| boolean       | isBefore(另一个LocalDate对象)<br />isAfter(另一个LocalDate对象) | 比较两个LocalDate对象前后关系                                |
| boolean       | isLeapYear()                                                 | 判断是否是闰年（在LocalDate类中声明）                        |
|               |                                                              |                                                              |
| LocalDateTime | atTime(int hour,  int minute, int second)                    | 基于当前日期指定时间返回一个LocalDateTime对象                |



### 5.3.3 java.time.LocalTime类

| 返回值        | 方法                                                         | **描述**                                                     |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| LocalTime     | now() <br />now(ZoneId zone)                                 | 静态方法，按照平台默认时区创建LocalTime对象<br />静态方法，按照指定时区创建LocalTime对象 |
| LocalTime     | of(int hour, int minute, int second)                         | 静态方法，根据指定时间创建LocalTime对象                      |
|               |                                                              |                                                              |
| int           | getHour()<br />getMinute()<br />getSecond()                  | 获取当前时间对象的小时值<br />获取当前时间对象的分钟值<br />获取当前时间对象的秒值 |
|               |                                                              |                                                              |
| LocalTime     | withHour(int hour)<br />withMinute(int minute)<br />withSecond(int second)<br />with(TemporalAdjuster  t) | 更改小时值返回一个新LocalTime对象<br />更改分钟值返回一个新LocalTime对象<br />更改秒值返回一个新LocalTime对象<br />更改时间值返回一个新LocalTime对象 |
| LocalTime     | plusHours(long hours)<br />plusMinutes(long minutes)<br />plusSeconds(long seconds)<br />plus(TemporalAmount t) | 增加几小时返回新LocalTime对象<br />增加几分返回新LocalTime对象<br />增加几秒返回新LocalTime对象<br />增加一个 Duration 返回新LocalTime对象 |
| LocalTime     | minusHours(long hours)<br />minusMinutes(long minutes)<br />minusSeconds(long seconds)<br />minus(TemporalAmount t) | 减少几小时返回新LocalTime对象<br />减少几分返回新LocalTime对象<br />减少几秒返回新LocalTime对象<br />减少一个 Duration 返回新LocalTime对象 |
|               |                                                              |                                                              |
| boolean       | isBefore(另一个LocalTime对象)<br />isAfter(另一个LocalTime对象) | 比较两个时间对象前后关系                                     |
|               |                                                              |                                                              |
| LocalDateTime | atDate(LocalDate date)                                       | 基于当前时间指定日期返回一个LocalDateTime对象                |



### 5.3.4 java.time.LocalDateTime类

| 返回值        | 方法                                                         | **描述**                                                     |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| LocalDateTime | now()<br />now(ZoneId zone)                                  | 静态方法，按照平台默认的时区创建LocalDateTime对象<br />静态方法，按照指定时区创建LocalDateTime对象 |
| LocalDateTime | of(int year, int month, int dayOfMonth, int hour, int minute, int second)<br />of(LocalDate date, LocalTime time) | 静态方法，根据指定日期时间创建LocalDateTime对象              |
|               |                                                              |                                                              |
| int           | getYear()<br />getMonthValue()<br />getDayOfMonth()<br />getDayOfYear()<br />getHour()<br />getMinute()<br />getSecond() | 获取年份值<br />获得月份(1-12)<br />获得在月份中的天数(1-31) <br />获得在年中的天数(1-366)<br />获取小时值<br />获取分钟值<br />获取秒值 |
| Month         | getMonth()                                                   | 获取月份对象, 返回一个Month枚举值                            |
| DayOfWeek     | getDayOfWeek()                                               | 获得星期几(返回一个 DayOfWeek 枚举值)                        |
|               |                                                              |                                                              |
| LocalDateTime | withYear(int year)<br />withMonth(int month)<br />withDayOfMonth(int dayOfMonth)<br />withDayOfYear(int dayOfYear)<br />withHour(int hour)<br />withMinute(int minute)<br />withSecond(int second)<br />with(TemporalAdjuster  t) | 更改年份值返回一个新LocalDateTime对象<br />更改月份值返回一个新LocalDateTime对象<br />更改日期值返回一个新LocalDateTime对象<br />更改当年第几天的值返回一个新LocalDateTime对象<br />更改小时值返回一个新LocalDateTime对象<br />更改分钟值返回一个新LocalDateTime对象<br />更改秒值返回一个新LocalDateTime对象<br /><br />更改日期时间值返回一个新LocalDateTime对象 |
| LocalDateTime | plusYears(long years)<br />plusMonths(long minute)<br />plusWeeks(long weeks)<br />plusDays(long days)<br />plusHours(long hours)<br />plusMinutes(long minutes)<br />plusSeconds(long seconds)<br />plus(TemporalAmount t) | 增加几年返回新LocalDateTime对象<br />增加几月返回新LocalDateTime对象<br />增加几周返回新LocalDateTime对象<br />增加几日返回新LocalDateTime对象<br />增加几小时返回新LocalDateTime对象<br />增加几分返回新LocalDateTime对象<br />增加几秒返回新LocalDateTime对象<br />增加一个Period或Duration返回新LocalDateTime对象 |
| LocalDateTime | minusYears(long years)<br />minusMonths(long minute)<br />minusWeeks(long weeks)<br />minusDays(long days)<br />minusHours(long hours)<br />minusMinutes(long minutes)<br />minusSeconds(long seconds)<br />minus(TemporalAmount t) | 减少几年返回新LocalDateTime对象<br />减少几月返回新LocalDateTime对象<br />减少几周返回新LocalDateTime对象<br />减少几日返回新LocalDateTime对象<br />减少几小时返回新LocalDateTime对象<br />减少几分返回新LocalDateTime对象<br />减少几秒返回新LocalDateTime对象<br />减少一个 Period或Duration返回新LocalDateTime对象 |
|               |                                                              |                                                              |
| boolean       | isBefore(另一个LocalDateTime对象)<br />isAfter(另一个LocalDateTime对象) | 比较两个LocalDateTime对象前后关系                            |
|               |                                                              |                                                              |
| LocalDateTime | ofInstant(Instant instant, ZoneId zone)                      | 从Instant和区域ID获取一个日期时间对象的实例。                |
| Instant       | toInstant(ZoneOffset offset)                                 | 指定时区偏移量返回一个Instant对象                            |
| LocalDate     | toLocalDate()                                                | 返回一个LocalDate对象                                        |
| LocalTime     | toLocalTime()                                                | 返回一个LocalTime对象                                        |
| ZonedDateTime | atZone(ZoneId zone)                                          | 将次日期时间与时区相结合以创建 ZonedDateTime，日期时间值不变，只是时区属性变了 |

### 5.3.5 java.time.ZoneId类

| 返回值      | 方法                  | 描述                                                       |
| ----------- | --------------------- | ---------------------------------------------------------- |
| ZoneId      | of(String zoneId)     | 静态方法，指定ID（例如Europe/Paris ）获取一个 ZoneId的实例 |
| ZoneId      | systemDefault()       | 静态方法，获取平台默认的时区                               |
| Set<String> | getAvailableZoneIds() | 静态方法，获取所有有效ID                                   |

### 5.3.6 java.time.ZoneOffset类

| 返回值     | 方法                | 描述                                                         |
| ---------- | ------------------- | ------------------------------------------------------------ |
| ZoneOffset | of(String offsetId) | 静态方法，指定偏移量id（ 例如：`+02:00` ）获取一个ZoneOffset的实例 |
| ZoneOffset | ofHours(int hours)  | 静态方法，指定小时偏移量获取一个ZoneOffset的实例             |



### 5.3.7 java.time.ZonedDateTime类

| 返回值        | 方法                                                         | **描述**                                                     |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ZonedDateTime | now()<br />now(ZoneId zone)                                  | 静态方法，按照平台默认的时区创建ZonedDateTime对象<br />静态方法，按照指定时区创建ZonedDateTime对象 |
| ZonedDateTime | of(int year, int month, int dayOfMonth, int hour, int minute, int second,int nanoOfSecond, ZoneId zone)<br />of(LocalDate date, LocalTime time, ZoneId zone)<br />of(LocalDateTime localDateTime, ZoneId zone) | 静态方法，根据指定日期时间和时区创建ZonedDateTime对象        |
|               |                                                              |                                                              |
| int           | getYear()<br />getMonthValue()<br />getDayOfMonth()<br />getDayOfYear()<br />getHour()<br />getMinute()<br />getSecond() | 获取年份值<br />获得月份(1-12)<br />获得在月份中的天数(1-31) <br />获得在年中的天数(1-366)<br />获取小时值<br />获取分钟值<br />获取秒值 |
| ZoneId        | getZone()                                                    | 获取时区                                                     |
| Month         | getMonth()                                                   | 获取月份对象, 返回一个Month枚举值                            |
| DayOfWeek     | getDayOfWeek()                                               | 获得星期几(返回一个 DayOfWeek 枚举值)                        |
|               |                                                              |                                                              |
| ZonedDateTime | withYear(int year)<br />withMonth(int month)<br />withDayOfMonth(int dayOfMonth)<br />withDayOfYear(int dayOfYear)<br />withHour(int hour)<br />withMinute(int minute)<br />withSecond(int second)<br />with(TemporalAdjuster  t) | 更改年份值、月份值等值返回一个新的ZonedDateTime对象          |
| ZonedDateTime | plusYears(long years)<br />plusMonths(long minute)<br />plusWeeks(long weeks)<br />plusDays(long days)<br />plusHours(long hours)<br />plusMinutes(long minutes)<br />plusSeconds(long seconds)<br />plus(TemporalAmount t) | 增加几年返回新ZonedDateTime对象<br />增加几月返回新ZonedDateTime对象<br />增加几周返回新ZonedDateTime对象<br />增加几日返回新ZonedDateTime对象<br />增加几小时返回新ZonedDateTime对象<br />增加几分返回新ZonedDateTime对象<br />增加几秒返回新ZonedDateTime对象<br />增加一个Period或Duration返回新ZonedDateTime对象 |
| ZonedDateTime | minusYears(long years)<br />minusMonths(long minute)<br />minusWeeks(long weeks)<br />minusDays(long days)<br />minusHours(long hours)<br />minusMinutes(long minutes)<br />minusSeconds(long seconds)<br />minus(TemporalAmount t) | 减少几年返回新ZonedDateTime对象<br />减少几月返回新ZonedDateTime对象<br />减少几周返回新ZonedDateTime对象<br />减少几日返回新ZonedDateTime对象<br />减少几小时返回新ZonedDateTime对象<br />减少几分返回新ZonedDateTime对象<br />减少几秒返回新ZonedDateTime对象<br />减少一个 Period或Duration返回新ZonedDateTime对象 |
|               |                                                              |                                                              |
| ZonedDateTime | ofInstant(Instant instant, ZoneId zone)                      | 从Instant和区域ID获取一个日期时间对象的实例。                |
| Instant       | toInstant(ZoneOffset offset)                                 | 指定时区偏移量返回一个Instant对象                            |
| LocalDate     | toLocalDate()                                                | 返回一个LocalDate对象                                        |
| LocalTime     | toLocalTime()                                                | 返回一个LocalTime对象                                        |
| LocalDateTime | toLocalDateTime()                                            | 返回一个LocalDateTime对象                                    |
| ZonedDateTime | withZoneSameInstant(ZoneId zone)                             | 返回同一时刻另一个时区的本地时间，时区不同，日期时间值不同   |
| ZonedDateTime | withZoneSameLocal(ZoneId zone)                               | 保留日期时间值，时区设置为另一个地方的时区                   |

### 5.3.8 java.time.Period类

| 返回值 | 方法                                                         | **描述**                                                     |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Period | between(LocalDate startDateInclusive, LocalDate endDateExclusive) | 静态方法，基于两个本地日期对象返回Period对象，代表一段日期间隔 |
| Period | of(int years, int months, int days)<br /><br />ofYears(int years)<br />ofMonths(int months)<br />ofWeeks(int weeks)<br />ofDays(int days) | 静态方法，基于years,months,weeks,days值创建Period对象        |
|        |                                                              |                                                              |
| int    | getYears()<br />getMonths()<br />getDays()                   | 获取年数、月份数、日子数                                     |
| long   | toTotalMonths()                                              | 获取总月份数                                                 |
|        |                                                              |                                                              |
| Period | withYears(int years)<br />withMonths(int months)<br />withDays(int days) | 更改年份值返回一个新Period对象<br />更改月份值返回一个新Period对象<br />更改日期值返回一个新Period对象 |
| Period | plusYears(long years)<br />plusMonths(long minutes)<br />plusDays(long days)<br />plus(TemporalAmount t) | 增加几年返回新Period对象<br />增加几月返回新Period对象<br />增加几日返回新Period对象<br />增加一个Period返回新Period对象 |
| Period | minusYears(long years)<br />minusMonths(long minutes)<br />minusDays(long days)<br />minus(TemporalAmount t) | 减少几年返回新Period对象<br />减少几月返回新Period对象<br />减少几日返回新Period对象<br />减少一个 Period返回新Period对象 |



### 5.3.9 java.time.Duration类 

| 返回值   | 方法                                                         | **描述**                                                     |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Duration | between(Temporal startInclusive, Temporal endExclusive)      | 静态方法，基于两个时间对象返回Duration对象，代表一段持续时间 |
| Duration | ofDays(long days)<br /><br />ofHours(long hours)<br />ofMinutes(long minutes)<br />ofSeconds(long seconds)<br /> | 静态方法，基于days，hours，minutes，seconds值创建Duration对象 |
|          |                                                              |                                                              |
| long     | toDays()<br />toHours()<br />toMinute()<br />toSeconds()     | 持续时间换算为天数、小时数、分钟数、秒数等，向下取整         |
|          |                                                              |                                                              |
| Duration | withSeconds(long seconds)                                    | 修改持续秒值返回新的Duration对象                             |
| Duration | plusDays(long days)<br />plusMinutes(long minutes)<br />plusSeconds(long seconds)<br />plusMillis(long millis)<br />plus(Duration t) | 增加几小时返回新Duration对象<br />增加几分钟返回新Duration对象<br />增加几秒钟返回新Duration对象<br />增加几毫秒返回新Duration对象<br />增加一个Duration返回新Duration对象 |
| Duration | minusDays(long years)<br />minusMinutes(long minutes)<br />minusSeconds(long days)<br />minusMillis(long millis)<br />minus(Duration t) | 减少几小时返回新Duration对象<br />减少几分钟返回新Duration对象<br />减少几秒钟返回新Duration对象<br />减少几毫秒返回新Duration对象<br />减少一个 Duration返回新Duration对象 |

### 5.3.10 java.time.format.FormatStyle枚举类

| 类型        | 常量   | **描述**                                                     |
| ----------- | ------ | ------------------------------------------------------------ |
| FormatStyle | FULL   | 全文风格，最多细节。例如，格式可能是“公元1952年4月12日星期二”或“太平洋标准时间下午3:30:42”。 |
| FormatStyle | LONG   | 长文字风格，有很多细节。例如，格式可能是“1952年1月12日”。    |
| FormatStyle | MEDIUM | 中等文字风格，有一些细节。例如，格式可能是“1952年1月12日”。  |
| FormatStyle | SHORT  | 短文本样式，通常为数字。例如，格式可能是“12 .13.52”或“下午3:30”。 |

### 5.3.11 java.time.format.DateTimeFormatter类

| 返回值            | 方法或常量                                                   | **描述**                                                     |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| DateTimeFormatter | BASIC_ISO_DATE <br />ISO_LOCAL_DATE<br />ISO_LOCAL_TIME<br />ISO_LOCAL_DATE_TIME<br />ISO_DATE<br />ISO_DATE<br />ISO_DATE_TIME<br />...... | 例如“20111203”<br />例如“2011-12-03”<br/>例如“10：15”或“10：15：30”<br />例如“2011-12-03T10：15：30” <br />例如“2011-12-03”或“2011-12-03 + 01：00”<br/>例如“10：15”，“10：15：30”或“10：15：30 + 01：00”<br/>例如“2011-12-03T10：15：30”，“2011-12-03T10：15：30 + 01：00”或“2011-12-03T10：15：30 + 01：00[欧洲/巴黎]”<br />...... |
|                   |                                                              |                                                              |
| DateTimeFormatter | ofPattern(String pattern)                                    | 静态方法，类似于SimpleDateFormat模式                         |
|                   |                                                              |                                                              |
| DateTimeFormatter | ofLocalizedDate(FormatStyle dateStyle)<br/>ofLocalizedTime(FormatStyle timeStyle)<br/>ofLocalizedDateTime(FormatStyle dateTimeStyle) | 静态方法，使用FormatStyle 枚举类对象创建DateTimeFormatter对象 |
|                   |                                                              |                                                              |
| DateTimeFormatter | withZone(ZoneId zone)                                        | 使用新的覆盖区域返回此格式化程序的副本。                     |
|                   |                                                              |                                                              |
| TemporalAccessor  | parse(CharSequence text)                                     | 将字符串解析为日期/时间对象                                  |
| String            | format(TemporalAccessor temporal)                            | 将日期/时间对象格式化成字符串                                |

# 六、比较器

## 6.1 java.lang.Comparable<T>接口

要比较大小的对象类本身实现这个接口。例如：学生类的对象要比较大小，就让学生类实现Comparable接口即可。

- int compareTo(T t)：如果this对象比t对象大，返回正整数；如果如果this对象比t对象小，返回负整数；如果this对象与t对象相等，返回零。

## 6.2 java.util.Comparator<T>接口

单独编写一个类实现Comparator接口，然后这个实现类的对象就相当于一个工具类，用于按照某个规则比较某个类的两个对象。例如：单独编写一个类StudentAgeComparator实现Comparator接口，用于按照年龄大小比较Student学生类两个对象的大小。

- int compare(T t1, T t2)：如果t1大于t2，返回正整数；如果t1小于t2，返回负整数；如果t1等于t2，返回零。

## 6.3 java.text.Collator类

字符串定制比较器。Collator 类执行区分语言环境的 String 比较。

- public static Collator getInstance()：获取平台默认语言环境的字符串比较器对象。
- public static Collator getInstance(Locale desiredLocale)：：获取指定语言环境的字符串比较器对象。
- public int compare(String source, String target)：比较两个字符串的大小。

# 七、数组工具类

## 7.1 java.lang.System类

- public static native void arraycopy(Object src,  int srcPos, Object dest, int destPos, int length)：从指定源数组src中复制length个元素到一个目标数组dest ， 将src数组的[srcPos, srcPos+length)元素复制到dest数组的[destPos, destPos+length)。

## 7.2 java.util.Arrays类

==注意：==所有方法，Arrays类都提供了八种基本数据类型的重载形式（下面只列出了int[]形式） 和 对象数组的重载形式。

### 1、拼接数组的元素

- public static String toString(int[] arr) ：将arr数组的元素列表，拼接为字符串形式，括在方括号（"[]"）中。相邻元素用字符 ", "（逗号加空格）分隔。形式为：[元素1，元素2，元素3。。。]。提供了八种基本数据类型的重载形式。
- public static String toString(Object[] arr) ：将对象数组arr数组的元素列表，拼接为字符串形式，括在方括号（"[]"）中。相邻元素用字符 ", "（逗号加空格）分隔。元素将自动调用自己从Object继承的toString方法将对象转为字符串进行拼接，如果没有重写，则返回类型@hash值，如果重写则按重写的toString方法返回的字符串进行拼接。

### 2、数组元素排序

- public static void sort(int[] arr) ：将arr数组中所有元素按照从小到大进行排序。

- public static void sort(int[] arr, int fromIndex, int toIndex) ：将arr数组的[fromIndex, toIndex)部分的元素按照升序排列。

  

- public static void sort(Object[] arr)：将对象数组arr所有元素按照元素的自然比较规则（即实现java.lang.Comparable接口的规则）进行升序排序。

- public static void sort(Object[] arr,int fromIndex,int toIndex)：将对象数组arr中[fromIndex, toIndex)部分的元素按照元素的自然比较规则（即实现java.lang.Comparable接口的规则）进行升序排序。

  

- public static <T> void sort(T[] arr,  Comparator<? super T>   comparator)：将对象数组arr所有元素按照定制比较器规则（即实现java.lang.Comparator接口的规则）进行升序排序。

- public static <T> void sort(T[] a,int fromIndex,int toIndex,Comparator<? super T> c)：将对象数组arr中[fromIndex, toIndex)部分的元素按照定制比较器规则（即实现java.lang.Comparator接口的规则）进行升序排序。

### 3、二分查找（首先要求数组必须有序）

- public static int binarySearch(int[] arr, int key) ：在arr数组中查找key的下标。如果有多个重复元素，返回第一次找到的。如果元素不存在，返回-插入点-1。所谓插入点就是如果将该元素插入到该数组中，它应该插入到哪个位置。

- public static int binarySearch(int[] a,int fromIndex,int toIndex,int key)：在arr数组[fromIndex, toIndex)范围查找key的下标。如果有多个重复元素，返回第一次找到的。如果元素不存在，返回-插入点-1。所谓插入点就是如果将该元素插入到该数组[fromIndex, toIndex)范围，它应该插入到哪个位置。

  

- public static int binarySearch(Object[] arr, Object key)：在对象数组arr中查找key的下标。使用元素的自然比较规则（即实现java.lang.Comparable接口的规则）比较元素大小。如果有多个重复元素，返回第一次找到的。如果元素不存在，返回-插入点-1。所谓插入点就是如果将该元素插入到该数组中，它应该插入到哪个位置。

- public static int binarySearch(Object[] arr, int fromIndex, int toIndex, Object key)：在对象数组arr的[fromIndex,toIndex)范围查找key的下标。使用元素的自然比较规则（即实现java.lang.Comparable接口的规则）比较元素大小。如果有多个重复元素，返回第一次找到的。如果元素不存在，返回-插入点-1。所谓插入点就是如果将该元素插入到该数组中，它应该插入到哪个位置。

  

- public static <T> int binarySearch(T[] arr, T key,Comparator<? super T> c)：在对象数组arr中查找key的下标。使用定制比较器的规则（即实现java.lang.Comparable接口的规则）比较元素大小。如果有多个重复元素，返回第一次找到的。如果元素不存在，返回-插入点-1。所谓插入点就是如果将该元素插入到该数组中，它应该插入到哪个位置。

- public static <T> int binarySearch(T[] arr, int fromIndex,int toIndex,T key,Comparator<? super T> c)：在对象数组arr的[fromIndex,toIndex)范围查找key的下标。使用定制比较器的规则（即实现java.lang.Comparable接口的规则）比较元素大小。如果有多个重复元素，返回第一次找到的。如果元素不存在，返回-插入点-1。所谓插入点就是如果将该元素插入到该数组中，它应该插入到哪个位置。

### 4、数组的复制

* public static int[] copyOf(int[] original, int newLength)  ：创建一个长度为newLength的新数组。如果newLength<=orginal.length，那么将原数组original的[0, newLength)范围的元素复制到新数组中。如果newLength>orginal.length，那么将原数组original的所有元素复制到新数组中，新数组剩下的元素都是默认值。最后返回新数组。

* public static int[] copyOfRange(int[] original, int from, int to) ：创建一个长度为to-from的新数组。如果from>=orginal.length，将会报错。如果to>orginal.length，则将原数组original的[from, orginal.length)范围的元素复制到新数组中。如果to<=orginal.length，则将原数组original的[from, to)范围的元素复制到新数组中。最后返回新数组。

  

* public static <T> T[] copyOf(T[] original,int newLength)：创建一个长度为newLength的新对象数组。如果newLength<=orginal.length，那么将原数组original的[0, newLength)范围的元素复制到新数组中。如果newLength>orginal.length，那么将原数组original的所有元素复制到新数组中，新数组剩下的元素都是默认值。最后返回新对象数组。

* public static <T> T[] copyOfRange(T[] original,int from,int to)：创建一个长度为to-from的新对象数组。如果from>=orginal.length，将会报错。如果to>orginal.length，则将原数组original的[from, orginal.length)范围的元素复制到新数组中。如果to<=orginal.length，则将原数组original的[from, to)范围的元素复制到新数组中。最后返回新对象数组。

### 5、比较两个数组是否相等

* public static boolean equals(int[] a1, int[] a2) ：比较两个数组的长度、元素是否完全相同
* public static boolean equals(Object[] a1,Object[] a2)：比较两个对象数组的长度、元素是否完全相同

### 6、填充数组

* public static void fill(int[] arr, int val) ：将arr数组所有元素赋值为val值。

* public static void fill(int[] arr, int fromIndex, int toIndex, int val)：将arr数组[fromIndex,toIndex)范围的元素赋值为val值。

  

* public static void fill(Object[] arr,Object val)：将arr数组所有元素赋值为val对象的首地址。

* public static void fill(Object[] arr, int fromIndex, int toIndex, Object val) ：将arr数组[fromIndex,toIndex)范围的元素赋值为val对象首地址。

  

* public static void setAll(int[] array, IntUnaryOperator generator)：将array数组的元素用generator生成器的结果覆盖。generator生成器必须重写IntUnaryOperator 接口的int applyAsInt(int index)抽象方法。在setAll方法中会遍历所有元素，并将数组元素下标作为实参传给applyAsInt方法，applyAsInt方法的返回值用于为[index]位置的元素赋值。

* setAll方法提供了4种重载形式，分别支持int[]、double[]、long[]、对象数组。

### 7、将元素添加到List集合

- public static <T> List<T> asList(T... args)：将对象数组args的所有对象添加到一个不可变的List集合中。



### 8、将数组元素添加到Stream流中

- public static IntStream stream(int[] array)：将array数组的元素添加到IntStream流中。
- public static IntStream stream(int[] array,int start,int end)：将array数组[start,end)范围的元素添加到IntStream流中。
- 该方法提供了4种重载形式，分别支持int[]、double[]、long[]、对象数组，分别返回IntStream、DoubleStream、LongStream、Stream。



# 八、字符串工具类

## 8.1 java.lang.String类

* `public String() ` ：初始化新创建的 String对象，以使其表示空字符序列。
* ` String(String original)`： 初始化一个新创建的 `String` 对象，使其表示一个与参数相同的字符序列；换句话说，新创建的字符串是该参数字符串的副本。
* `public String(char[] value) ` ：通过当前参数中的字符数组来构造新的String。
* `public String(char[] value,int offset, int count) ` ：通过字符数组的一部分来构造新的String。
* `public String(byte[] bytes) ` ：通过使用运行环境的默认字符集解码当前参数中的字节数组来构造新的String。
* `public String(byte[] bytes,String charsetName) ` ：通过使用指定的字符集解码当前参数中的字节数组来构造新的String。
* public boolean isEmpty()：判断字符串是否为空字符串，这里的空字符串是说长度为0的字符串。
* public boolean isBlank()：判断字符串中是否除了空白字符，没有别的字符。长度不一定为0。
* public int length()：获取字符串的长度，即字符串中字符的个数。
* public String toUpperCase()：根据当前字符串文本返回大写形式的字符串。
* public String toLowerCase()：根据当前字符串文本返回小写形式的字符串。
* public String trim()：去掉当前字符串中前后空白符返回新字符串对象。如果当前字符串前后没有空白符，则返回原字符串对象。
* public char charAt(int index)：获取[index]位置的字符
* public char[] toCharArray()：将字符串中的字符放到一个char[]数组中返回。
* public boolean equals(Object o)：判断两个字符串的内容、长度、顺序、大小写是否完全一致。重写Object类的equals方法。
* public boolean equalsIgnoreCase(Object o)：忽略大小写比较两个字符串的内容，当然要求长度、顺序要完全一致。
* public int compareTo(Object obj)：重写Comparable接口的抽象方法，用于比较字符串大小。按照字符的编码值比较大小，长的字符串与短的字符串前面的字符全部都相同，那么按照长度比较大小，短的小，长的大。
* public int compareToIgnoreCase(String o)：不区分大小写的字符串比较大小。
* public boolean startWith(String s)：判断当前字符串是否以s开头
* public boolean endsWith(String s)：判断当前字符串是否以s结尾
* public String substring(int index)：从当前字符串[index]开始截取到最后构成新字符串。
* public String substring(int start, int  end)：从当前字符串截取[start ,end)部分的字符构成新字符串，Java中凡是表示区间的都是左闭右开。
* public boolean contains(CharSequence obj)：判断当前字符串中是否包含obj子串。
* public int indexOf(String s)：查找子串s在当前字符串中的下标，如果出现多个s，返回左边第一次出现的下标
* public int lastIndexOf(String s)：查找子串s在当前字符串中的下标，如果出现多个s，返回最右边或最后一次出现的下标
* public byte[] getBytes()：按照程序运行环境默认的编码方式把字符串转为字节数组，例如IDEA设置的UTF-8。
* public byte[] getBytes(String charset)：按照指定的编码方式把字符串转为字节数组，例如：GBK。
  * 编码：把字符序列转为字节序列，为了网络传输，文件的读写。
  * 解码：把字节序列转为字符序列，为了给人看。
* public boolean matches(正则表达式)：判断当前字符串是否匹配某个正则表达式。
* public String[] split(正则表达式)：把当前字符串按照某个规则拆分为多个字符串。
* public String replace(char oldChar, char newChar)：把当前字符串中oldChar字符替换为newChar。
* public String replaceFirst(正则表达式,  String newStr)：把当前字符串中第一个满足该规则的字符替换为newStr。
* public String replaceAll(正则表达式,  String newStr)：把当前字符串中所有满足该规则的字符替换为newStr。

- public String concat(String s)：将当前字符串与s字符串拼接构成新字符串。
- public String intern()：在字符串常量池中查找是否有与当前字符串相同的字符串，如果有返回常量池中那个字符串的首地址；如果没有，将当前放入字符串常量池，并返回其首地址。

## 8.2 java.lang.StringBuffer类

- public StringBuffer() ：构造一个没有字符的字符串缓冲区，初始容量为16个字符。 

- public StringBuffer(CharSequence seq) ：构造一个包含与指定的相同字符的字符串缓冲区 CharSequence 。 

- public StringBuffer(int capacity) 构造一个没有字符的字符串缓冲区和指定的初始容量。 

- public StringBuffer(String str) ：构造一个初始化为指定字符串内容的字符串缓冲区。 

- public StringBuffer append(各种数据类型的值)：在当前字符串末尾追加（即拼接）某个值。

- public StringBuffer insert(int index, 各种数据类型的值：在[index]位置插入某个值。

- public StringBuffer delete(int start, int end)：删除[start,end)之间字符。

- public StringBuffer deleteCharAt(int index)：删除[index]位置字符。

- public void setCharAt(int index, xx)：替换[index]位置字符。

- public StringBuffer reverse()：将当前字符串中的字符顺序反转。

- public void setLength(int newLength) ：设置当前字符序列长度为newLength。

- public StringBuffer replace(int start, int end, String str)：替换[start,end)范围的字符序列为str。

- public int indexOf(String str)：在当前字符序列中查询str的第一次出现下标。

- public int indexOf(String str, int fromIndex)：在当前字符序列[fromIndex,最后]中查询str的第一次出现下标。

- public int lastIndexOf(String str)：在当前字符序列中查询str的最后一次出现下标。

- public int lastIndexOf(String str, int fromIndex)：在当前字符序列[fromIndex,最后]中查询str的最后一次出现下标。

- public String substring(int start)：截取当前字符串[start,最后]部分的字符构成String字符串对象。

- public String substring(int start, int end)：截取当前字符串[start,end)部分的字符构成String字符串对象。

- public String toString()：将当前StringBuffer对象中的所有字符序列构建为String对象返回。

- public void trimToSize()：尝试减少用于字符序列的存储空间。如果缓冲区大于保存当前字符序列所需的存储空间，则将重新调整其大小，以便更好地利用存储空间。


## 8.3 java.lang.StringBuilder类

StringBuilder类的API与StringBuffer类完全兼容，即上述API方法将StringBuffer换成StringBuilder即可。只是StringBuffer是线程安全的，StringBuilder是线程不安全的。

# 九、Objects工具类

JDK1.7引入，用于判断对象是否为空，计算对象hash值，比较两个对象大小、是否相等，返回对象toString结果。

- public static boolean isNull(Object obj)：判断某个对象是否为null，如果为null返回true，否则返回false。
- public static boolean nonNull(Object obj)：判断某个对象是否非null，如果非null返回true，否则返回false。
- public static int hashCode(Object o)：计算某个对象的哈希值。
- public static int hash(Object... values)：计算一组对象的哈希值。
- public static <T> int compare(T a, T b, Comparator<? super T> c)：用指定比较器比较两个对象的大小关系。
- public static boolean equals(Object a, Object b)：比较两个对象是否相等。
- public static String toString(Object o)：如果对象o为null，则返回"null"，否则返回o.toString()结果。
- public static String toString(Object o, String nullDefault)：如果对象o不为null，返回o.toString()结果，否则返回nullDefault值。

# 十、集合

## 10.1 集合框架图

![集合框架集图片](JavaSE常用API文档.assets/集合框架集图片.png)

## 10.2 java.lang.Iterable<T>接口

实现这个接口的对象就可以使用Iterator迭代器进行遍历。

实现这个接口允许对象成为 "foreach" 语句的目标。 

- public Iterator<T> iterator()：返回一个迭代器对象，用于遍历容器中的元素。
- public default void forEach(Consumer<? super T> action)：将action指定的操作应用到容器中的所有元素上。

## 10.3 java.util.Iterator<E>接口

- public boolean hasNext()：如果仍有元素可以迭代，则返回 true。 
- public E next() ：返回当前元素，并让迭代器指向下一个元素。 
- public void remove()：从迭代器指向的容器中移除迭代器最后返回的元素。

## 10.4 java.util.Collection<E>接口

### 1、添加元素

- public boolean add(E e)：添加一个元素。


- public boolean addAll(Collection<? extends E> c)：添加一组元素。即把c集合中的一组元素添加到当前集合(this)。 this = this ∪ c


### 2、删除元素

- public void clear()：清空所有元素。

- public boolean remove(Object o)：在当前集合中找到和o相等的一个元素，然后删除它，并返回true。如果没找到，返回false。

- public boolean removeAll(Collection<?> c)：从当前集合中删除所有和c集合中“相同的”元素。this = this - this ∩ c。

- public boolean retainAll(Collection<?> c)：从当前集合中删除和所有和c集合中“不同的”元素，即当前集合中只留下和c集合相同的元素。this = this ∩ c。

- public default boolean removeIf(Predicate<? super E> filter)：JDK8引入的。从当前集合中删除Predicate接口的实现类的test方法判断为true的元素。在Predicate接口的实现类中会重写一个boolean test(E element)方法，该方法用于判断当前集合的元素是否满足xx条件。在removeIf方法中，会遍历集合所有元素，并将元素作为实参传给test方法，如果该元素满足test方法中的条件，则返回true，该元素就会被删除；该元素不满足test方法中的条件，则返回false，该元素就会被保留。

### 3、查询元素

- public boolean contains(Object obj)：用于判断当前集合是否包含obj这个对象。
- public boolean containsAll(Collection<?> c)：用于判断当前集合是否包含c集合的所有对象。即判断c集合是否是当前集合的“子集”。如果c是this的子集，返回true，否则返回false。

- public boolean isEmpty()：判断当前集合是否为空。

- public int size()：用于返回当前集合的元素的总个数。

- public Object[] toArray() ：把当前集合中所有元素放到一个Object[]数组中返回。
- public <T> T[] toArray(T[] a)：把当前集合中所有元素放到一个T[]数组中返回。T类型是可以兼容集合元素的任意类型。

### 4、遍历

- foreach循环遍历
- public Iterator<T> iterator()：返回一个Iterator迭代器对象，用于遍历容器中的元素。

## 10.5 java.util.Set<E>接口

Set<E>是Collection<E>的子接口。Set接口的API和Collection接口完全相同。

## 10.6 java.util.SortedSet<E>接口

SortedSet<E>是Set<E>的子接口。

- public Comparator<? super E> comparator()：返回用于对该集合中的元素进行排序的定制比较器对象。如果此集合使用元素的自然比较顺序，则返回null。 
- public E first() ：返回此当前集合的第一个元素。
- public E last()  ：返回此当前集合的最后一个元素。
- public SortedSet<E> headSet(E toElement)：返回当前之前排在toElement元素之前的所有元素。
- public SortedSet<E> tailSet(E fromElement)：返回当前之前排在fromElement元素之后的所有元素。
- public SortedSet<E> subSet(E fromElement, E toElement)：返回当前之前排在[fromElement,toElement)之间的所有元素。  

## 10.7 java.util.List<E>接口

List<E>是Collection<E>的子接口。Collection<E>接口中的所有方法，List<E>接口都有。另外，List<E>接口还包含如下方法：

### 1、添加

* public void add(int index, E element)：把新元素element添加到指定到当前集合列表的[index]位置。
* public boolean addAll(int index, Collection<? extends E> c)：将c集合的所有元素添加到指定到当前集合列表的[index]位置。

### 2、删除

- public E remove(int index)：删除当前集合列表中[index]位置的元素，并返回被删除元素。

### 3、修改

- public E set(int index, E ele)：替换当前集合列表中[index]位置的元素，并返回被替换的元素。
- public default void replaceAll(UnaryOperator<E> operator)：JDK8引入的。实现UnaryOperator接口时必须重写public E apply(E oldValue) 方法。在replaceAll方法中会遍历集合的所有元素，并将每一个元素作为实参传给apply方法，然后用apply方法的返回值作为newValue替换该元素。
- pubilc default void sort(Comparator<? super E> c)：使用定制比较器对象c，对当前集合列表的元素排序。

### 4、查询

- public E get(int index)：返回当前集合列表中[index]位置的元素
- public List subList(int fromIndex, int toIndex)：返回当前集合列表中[fromIndex, toIndex)范围的元素

* public int indexOf(Object obj)：在当前集合列表中查询obj元素的位置，如果存在多个obj，则返回第1次出现的位置。
* int lastIndexOf(Object obj)：在当前集合列表中查询obj元素的位置，如果存在多个obj，则返回最后1次出现的位置。

### 5、遍历

- foreach循环遍历
- public Iterator<T> iterator()：返回一个Iterator迭代器对象，用于遍历容器中的元素。
- 普通for循环+list.size()+list.get(下标)
- public ListIterator<E> listIterator()：返回一个ListIterator迭代器对象。用于遍历容器中的元素。一开始ListIterator迭代器游标默认在集合的第一个元素位置。
- public ListIterator<E> listIterator(int index)：返回一个ListIterator迭代器对象。用于遍历容器中的元素。一开始ListIterator迭代器游标默认[index]位置。

## 10.8 java.util.ListIterator<E>接口

ListIterator<E>是Iterator<E>的子接口。

- public boolean hasNext()：以正向遍历列表，往后仍有元素可以迭代，则返回 true。 

- public E next() ：以正向遍历列表，返回迭代器指向的当前元素，并让迭代器指向下一个元素。

- public int nextIndex()：以正向遍历列表，返回迭代器指向的当前元素的索引。

  

- public boolean hasPrevious()：以逆向遍历列表，往前仍有元素可以迭代，则返回true。

- public Object previous()：以逆向遍历列表，返回迭代器前面的一个元素。

- public int previousIndex()：以逆向遍历列表，返回迭代器前面一个元素的索引。

  

- public void add(E e)：在迭代器当前位置添加元素e到对应集合。

- public void set(Object obj)：通过迭代器替换迭代器最后返回的元素。

- public void remove()：从当前列表迭代器指向的容器中移除迭代器最后返回的元素。



## 10.9 java.util.Stack<E>类

Stack用以描述一个堆栈结构的容器，元素具有先进后出（FILO）的特点。

- public E push(E item)：将元素添加到此堆栈的顶部。  
- public E pop()：删除此堆栈顶部的对象，并返回该对象
- public E peek()：查看此堆栈顶部的对象，而不从堆栈中删除它。  
- public boolean empty()：测试此堆栈是否为空。  
- public int search(Object o)：返回对象o在此堆栈的位置。栈顶为1。  

## 10.10 java.util.Queue<E>接口

Queue用以描述一个队列结构的容器，元素具有先进先出（FIFO）的特点。Queue<E>也是Collection<E>接口的子接口，所以Queue接口也具有Collection接口的方法。

### 1、失败抛出异常

- public boolean add(E e)：将指定的元素插入到此队列中，如果当前容器没有容量限制，添加成功则返回true，如果没有空间可用，则抛出IllegalStateException。  
- public E remove()：删除并返回队头元素。 如果队列没有元素，则抛出NoSuchElementException异常
- public E element()：查看队头的元素，但不删除。  如果队列没有元素，则抛出NoSuchElementException异常。

### 2、失败返回特殊值

- public boolean offer(E e)：如果在不违反容量限制的情况下将指定的元素插入到此队列中，并返回true，否则返回false。 
- public E poll()：删除并返回队头元素。 如果队列没有元素，则返回 null 。
- public E peek()：查看队头的元素，但不删除。  如果队列没有元素，则返回 null 。  

 

## 10.11 java.util.Deque<E>接口

Deque用以描述一个双端队列结构的容器，元素既可以从队头添加和删除，也可以从队尾添加和删除。Deque<E>也是Collection<E>和Queue<E>接口的子接口，所以Deque接口也具有Collection<E>和Queue<E>接口的方法。

### 1、失败抛出异常

- public void addFirst(E e)：如果没有容量限制，将元素插入此双端队列的最前面。如果没有可用容量，则抛出IllegalStateException。  
- public void addLast(E e)：如果没有容量限制，将元素插入此双端队列的最后面。如果没有可用容量，则抛出IllegalStateException。  
- public E removeFirst()：返回并删除此双端队列最前面的元素。如果没有元素，则抛出NoSuchElementException异常。
- public E removeLast()：返回并删除此双端队列最后面的元素。如果没有元素，则抛出NoSuchElementException异常
- public E getFirst()：返回但不删除此双端队列最前面的元素。如果没有元素，则抛出NoSuchElementException异常。
- public E getLast()：返回但不删除此双端队列最后面的元素。如果没有元素，则抛出NoSuchElementException异常。



### 2、失败返回特殊值

- public boolean offerFirst(E e)：如果没有容量限制，将元素插入此双端队列的最前面，并返回true，否则返回false。
- public boolean offerLast(E e)：如果没有容量限制，将元素插入此双端队列的最后面，并返回true，否则返回false。
- public E pollFirst()：返回并删除此双端队列最前面的元素。如果没有元素，则返回null。
- public E pollLast()：返回并删除此双端队列最后面的元素。如果没有元素，则返回null。
- public boolean removeFirstOccurrence(Object o)：如果o存在于此双端队列中，则删除它第一次。如果不存在，什么也不干。
- public boolean removeLastOccurrence(Object o)：如果o存在于此双端队列中，则删除它最后一次。如果不存在，什么也不干。
- public E peekFirst()：返回但不删除此双端队列最前面的元素。如果没有元素，则返回null。
- public E peekLast()：返回但不删除此双端队列最后面的元素。如果没有元素，则返回null。

## 10.12 java.util.Map<K,V>接口

java.util.Map<K,V>接口，是Map系列集合的根接口，这个系列的集合用于存储 键值对或 映射关系，(key,value)，即每一个key对应一个value,或者说每一个key会映射到一个value上。

Map系列的集合有一个共同特点：key不可重复。如果key重复了，后面的value会覆盖/替换原来的value。

### 1、添加

* public V put(K key, V value)：添加一对键值对。如果是首次添加这个key的映射关系，那么返回值是null。如果这个key的映射关系已存在，返回被覆盖/替换的value值。
* public void putAll(Map<? extends K,? extends V> m)：添加一组键值对。如果m集合中有key与当前map的key重复，会覆盖当前集合中的(key,value)。

### 2、删除

* public void clear()：清空当前map。
* public V remove(Object key)：根据key删除一对键值对。如果该key的映射关系存在，那么会移除一对映射关系，并且返回value值。如果该key的映射关系不存在，返回null。
* public default boolean remove(Object key,Object value)：删除匹配的(key,value)键值对。该方法是JDK8引入的。

### 3、修改

- 如果你是key不变，修改value，可以再次put一下新的(key,value)。
- public default V replace(K key, V value)：找到目标key，替换value。
- public default boolean replace(K key,V oldValue,V newValue)：找到目标(key,value)，替换value。
- public default void replaceAll(BiFunction<? super K,? super V,? extends V> function)：实现BiFunction接口并重写R apply(T t, U u)方法（此时为public String apply(Integer key, String oldValue)形式）。在replaceAll方法中会遍历当前map，并将每一个(key,value)作为实参传给apply方法，然后将apply方法的返回值作为newValue覆盖当前oldValue。

### 4、查询

* public V get(Object key)：根据key返回value。
* public default V getOrDefault(Object key,V defaultValue)：如果根据key可以get到一个非null的value值，则返回value值，否则返回defaultValue。
* public boolean containsKey(Object key)：判断key是否存在。
* public boolean containsValue(Object value)：判断value是否存在。
* public boolean isEmpty()：判断map是否为空。
* public int size()：获取键值对的数量。

### 5、遍历

==注意==：Map接口并没有继承Iterarble接口，所以不能直接使用foreach或Iterator迭代器遍历。

（1）分开遍历：

* public Set<K> keySet()：返回当前map中的所有key构成的Set集合，然后可以遍历所有的key。
* public Collection<V> values()：返回当前map中的所有value构成的Collection集合，然后遍历所有value。

（2）成对遍历：

* public default void forEach(BiConsumer<? super K,? super V> action)：实现BiConsumer接口的void accept(T t, U u)抽象方法（此时为public void accept(Integer key, String value)形式）。在forEach方法中会遍历当前map的所有键值对，并将每一对键值对(key,value)作为实参传给accept方法。
* public Set<Map.Entry<K,V>> entrySet()：返回当前map中所有键值对Entry对象构成的Set集合，然后遍历所有键值对的Entry对象。
* 遍历的是映射关系Map.Entry类型的对象，Map.Entry是Map接口的内部接口。每一种Map内部有自己的Map.Entry的实现类。在Map中存储数据，实际上是将Key---->value的数据存储在Map.Entry接口的实例中，再在Map集合中插入Map.Entry的实例化对象，如图示： 

![1563725601891](JavaSE常用API文档.assets/1563725601891.png)

### 6、其他

- public default V putIfAbsent(K key, V value)：先用该key从当前map中get到oldValue值。如果该oldValue值为null，那么将(key,value)映射关系==put==到当前map中。如果该oldValue值不为null，那么==不覆盖==value。最后putIfAbsent方法返回oldValue值。
- public default V merge(K key,V value,BiFunction<? super V,? super V,? extends V> remappingFunction)：实现BiFunction接口并重写R apply(T t, U u)方法（此时为public String apply(String oldValue, String value) 形式）。在merge方法中，先用该key从当前map中查询oldValue值，如果oldValue为null，则将(key,value)映射关系==put==到当前map中，最后merge方法返回value值；如果oldValue不为null，则将(oldValue，value)作为实参传给apply方法，并用apply方法的返回值作为newValue覆盖oldValue，最后merge方法返回newValue值。
- public default V computeIfPresent(K key,BiFunction<? super K,? super V,? extends V> remappingFunction)：实现BiFunction接口并重写R apply(T t, U u)方法（此时为public String apply(Integer key, String oldValue)形式）。在computeIfPresent，先用该key从当前map中查询oldValue值，如果oldValue为null，则什么也不干，最后computeIfPresent方法返回null；如果oldValue不为null，则将(key，oldValue)作为实参传给apply方法，并用apply方法的返回值作为newValue==覆盖==oldValue，最后computeIfPresent方法返回newValue。
- public default V computeIfAbsent(K key,Function<? super K,? extends V> mappingFunction)：实现BiFunction接口并重写R apply(T t, U u)方法（此时为public String apply(Integer key)形式）。在computeIfPresent，先用该key从当前map中查询oldValue值，如果oldValue不为null，则什么也不干，最后computeIfAbsent方法返回oldValue；如果oldValue为null，则将(key)作为实参传给apply方法，并用apply方法的返回值作为newValue，将(key,newValue)映射关系==put==到当前map中，最后computeIfAbsent方法返回newValue。
- public default V compute(K key, BiFunction<? super K,? super V,? extends V> remappingFunction) ：实现BiFunction接口并重写R apply(T t, U u)方法（此时为public String apply(Integer key, String oldValue)形式）。在computeIfPresent，先用该key从当前map中查询oldValue值，再将(key, oldValue)作为实参传给apply方法，然后用apply方法的返回值作为newValue，并将(key,  newValue)映射关系==put==到当前map中，最后compute方法返回newValue。



## 10.13 java.util.Map.Entry<E,V>接口

Map.Entry<E,V>接口是Map<K,V>接口的静态内部接口。

- public K getKey()：返回与此键值对的key键。 
- public V getValue()：返回与此键值对的value值。 
- public V setValue(V value)：替换此键值对的value值。

## 10.14 java.util.SortedMap<K,V>接口

SortedMap<K,V>接口是Map<K,V>的子接口。Map接口的方法，它也有，如下是它新增的方法：

public Comparator<? super K> comparator()：返回用于当前map中的比较器。 如果此集合使用元素的自然比较顺序，则返回null。

public K firstKey()：返回当前map中当前的第一个（最低）键。 

public SortedMap<K,V> headMap(K toKey)：返回当前map中key小于 toKey 的键值对。 

public K lastKey()：返回当前map中的最后（最高）键。 

public SortedMap<K,V> subMap(K fromKey, K toKey)：返回当前map中key在[fromKey ,toKey )范围的键值对。 

public SortedMap<K,V> tailMap(K fromKey)：返回当前map中key大于 fromKey的键值对。 

## 10.15 java.util.Collections类

Collections类似于Arrays，只是一个工具类，它是专门用于为各种集合服务的工具类。

Collections 是一个操作 Set、List 和 Map 等集合的工具类。Collections 中提供了一系列静态的方法对集合元素进行排序、查询和修改等操作，还提供了对集合对象设置不可变、对集合对象实现同步控制（线程安全）等方法：

* public static <T> boolean addAll(Collection<? super T> c,T... elements)：将所有指定元素添加到指定 collection 中。
* public static <T> int binarySearch(List<? extends Comparable<? super T>> list,T key)：在List集合中查找某个元素的下标，List的元素必须支持可比较大小，即支持自然排序。而且List集合也事先必须是有序的，否则结果不确定。
* public static <T> int binarySearch(List<? extends T> list,T key,Comparator<? super T> c)：在List集合中查找某个元素的下标，List的元素使用定制比较器c的compare方法比较大小。而且List集合也事先必须是有序的，否则结果不确定。

* public static <T extends Object & Comparable<? super T>> T max(Collection<? extends T> coll)在coll集合中找出最大的元素，集合中的对象必须是T或T的子类对象，而且支持自然排序
* public static <T> T max(Collection<? extends T> coll,Comparator<? super T> comp)在coll集合中找出最大的元素，集合中的对象必须是T或T的子类对象，按照比较器comp找出最大者
* public static void reverse(List<?> list)反转指定列表List中元素的顺序。
* public static void shuffle(List<?> list) List 集合元素进行随机排序，类似洗牌
* public static <T extends Comparable<? super T>> void sort(List<T> list)根据元素的自然顺序对指定 List 集合元素按升序排序
* public static <T> void sort(List<T> list,Comparator<? super T> c)根据指定的 Comparator 产生的顺序对 List 集合元素进行排序
* public static void swap(List<?> list,int i,int j)将指定 list 集合中的 i 处元素和 j 处元素进行交换
* public static int frequency(Collection<?> c,Object o)返回指定集合中指定元素的出现次数
* public static <T> void copy(List<? super T> dest,List<? extends T> src)将src中的内容复制到dest中
* public static <T> boolean replaceAll(List<T> list，T oldVal，T newVal)：使用新值替换 List 对象的所有旧值
* Collections 类中提供了多个 synchronizedXxx() 方法，该方法可使将指定集合包装成线程同步的集合，从而可以解决多线程并发访问集合时的线程安全问题
* Collections类中提供了多个unmodifiableXxx()方法，该方法返回指定 Xxx的不可修改的视图。



# 十一、Lambda表达式与StreamAPI

## 11.1 函数式接口

### 11.1.1 消费型接口

消费型接口的抽象方法特点：有形参，但是返回值类型是void

| 序号 | 接口名               | 抽象方法                       | 描述                       |
| ---- | -------------------- | ------------------------------ | -------------------------- |
| 1    | Consumer<T>          | void accept(T t)               | 接收一个对象用于完成功能   |
| 2    | BiConsumer<T,U>      | void accept(T t, U u)          | 接收两个对象用于完成功能   |
| 3    | DoubleConsumer       | void accept(double value)      | 接收一个double值           |
| 4    | IntConsumer          | void accept(int value)         | 接收一个int值              |
| 5    | LongConsumer         | void accept(long value)        | 接收一个long值             |
| 6    | ObjDoubleConsumer<T> | void accept(T t, double value) | 接收一个对象和一个double值 |
| 7    | ObjIntConsumer<T>    | void accept(T t, int value)    | 接收一个对象和一个int值    |
| 8    | ObjLongConsumer<T>   | void accept(T t, long value)   | 接收一个对象和一个long值   |

### 11.1.2 供给型接口

供给型接口的抽象方法特点：无参，但是有返回值

| 序号 | 接口名          | 抽象方法               | 描述              |
| ---- | --------------- | ---------------------- | ----------------- |
| 1    | Supplier<T>     | T get()                | 返回一个对象      |
| 2    | BooleanSupplier | boolean getAsBoolean() | 返回一个boolean值 |
| 3    | DoubleSupplier  | double getAsDouble()   | 返回一个double值  |
| 4    | IntSupplier     | int getAsInt()         | 返回一个int值     |
| 5    | LongSupplier    | long getAsLong()       | 返回一个long值    |

### 11.1.3 判断型接口

判断型接口的抽象方法特点：有参，但是返回值类型是boolean结果。

| 序号 | 接口名           | 抽象方法                   | 描述             |
| ---- | ---------------- | -------------------------- | ---------------- |
| 1    | Predicate<T>     | boolean test(T t)          | 接收一个对象     |
| 2    | BiPredicate<T,U> | boolean test(T t, U u)     | 接收两个对象     |
| 3    | DoublePredicate  | boolean test(double value) | 接收一个double值 |
| 4    | IntPredicate     | boolean test(int value)    | 接收一个int值    |
| 5    | LongPredicate    | boolean test(long value)   | 接收一个long值   |

### 11.1.4 功能型接口

功能型接口的抽象方法特点：既有参数又有返回值。

- 以Operator单词结尾的函数式接口，它的抽象方法的形参类型与返回值类型是一样的。
- 以Bi开头或中间包含Bi的函数式接口，它的抽象方法有两个形参
- 以To开始或中间包含To的函数式接口，它的抽象方法的返回值类型是to后面的类型

| 序号 | 接口名                  | 抽象方法                                        | 描述                                                |
| ---- | ----------------------- | ----------------------------------------------- | --------------------------------------------------- |
| 1    | Function<T,R>           | R apply(T t)                                    | 接收一个T类型对象，返回一个R类型对象结果            |
| 2    | UnaryOperator<T>        | T apply(T t)                                    | 接收一个T类型对象，返回一个T类型对象结果            |
| 3    | DoubleFunction<R>       | R apply(double value)                           | 接收一个double值，返回一个R类型对象                 |
| 4    | IntFunction<R>          | R apply(int value)                              | 接收一个int值，返回一个R类型对象                    |
| 5    | LongFunction<R>         | R apply(long value)                             | 接收一个long值，返回一个R类型对象                   |
| 6    | ToDoubleFunction<T>     | double applyAsDouble(T value)                   | 接收一个T类型对象，返回一个double                   |
| 7    | ToIntFunction<T>        | int applyAsInt(T value)                         | 接收一个T类型对象，返回一个int                      |
| 8    | ToLongFunction<T>       | long applyAsLong(T value)                       | 接收一个T类型对象，返回一个long                     |
| 9    | DoubleToIntFunction     | int applyAsInt(double value)                    | 接收一个double值，返回一个int结果                   |
| 10   | DoubleToLongFunction    | long applyAsLong(double value)                  | 接收一个double值，返回一个long结果                  |
| 11   | IntToDoubleFunction     | double applyAsDouble(int value)                 | 接收一个int值，返回一个double结果                   |
| 12   | IntToLongFunction       | long applyAsLong(int value)                     | 接收一个int值，返回一个long结果                     |
| 13   | LongToDoubleFunction    | double applyAsDouble(long value)                | 接收一个long值，返回一个double结果                  |
| 14   | LongToIntFunction       | int applyAsInt(long value)                      | 接收一个long值，返回一个int结果                     |
| 15   | DoubleUnaryOperator     | double applyAsDouble(double operand)            | 接收一个double值，返回一个double                    |
| 16   | IntUnaryOperator        | int applyAsInt(int operand)                     | 接收一个int值，返回一个int结果                      |
| 17   | LongUnaryOperator       | long applyAsLong(long operand)                  | 接收一个long值，返回一个long结果                    |
|      |                         |                                                 |                                                     |
| 18   | BiFunction<T,U,R>       | R apply(T t, U u)                               | 接收一个T类型和一个U类型对象，返回一个R类型对象结果 |
| 19   | BinaryOperator<T>       | T apply(T t, T u)                               | 接收两个T类型对象，返回一个T类型对象结果            |
| 20   | ToDoubleBiFunction<T,U> | double applyAsDouble(T t, U u)                  | 接收一个T类型和一个U类型对象，返回一个double        |
| 21   | ToIntBiFunction<T,U>    | int applyAsInt(T t, U u)                        | 接收一个T类型和一个U类型对象，返回一个int           |
| 22   | ToLongBiFunction<T,U>   | long applyAsLong(T t, U u)                      | 接收一个T类型和一个U类型对象，返回一个long          |
| 23   | DoubleBinaryOperator    | double applyAsDouble(double left, double right) | 接收两个double值，返回一个double结果                |
| 24   | IntBinaryOperator       | int applyAsInt(int left, int right)             | 接收两个int值，返回一个int结果                      |
| 25   | LongBinaryOperator      | long applyAsLong(long left, long right)         | 接收两个long值，返回一个long结果                    |



## 11.2 StreamAPI

Stream API ( java.util.stream) 把真正的函数式编程风格引入到Java中。这是目前为止对Java类库最好的补充，因为Stream API可以极大提高Java程序员的生产力，让程序员写出高效率、干净、简洁的代码。

Stream 是 Java8 中处理集合的关键抽象概念，它可以指定你希望对集合进行的操作，可以执行非常复杂的查找、过滤和映射数据等操作。 使用Stream API 对集合数据进行操作，就类似于使用 SQL 执行的数据库查询。也可以使用 Stream API 来并行执行操作。简言之，Stream API 提供了一种高效且易于使用的处理数据的方式。

Stream是数据渠道，用于操作数据源（集合、数组等）所生成的元素序列。“集合讲的是数据，负责存储数据，Stream流讲的是计算，负责处理数据！”

注意：

①Stream 自己不会存储元素。

②Stream 不会改变源对象。每次处理都会返回一个持有结果的新Stream。

③Stream 操作是延迟执行的。这意味着他们会等到需要结果的时候才执行。

### 11.2.1 创建StreamAPI

**1、创建 Stream方式一：通过集合**

Java8 中的 Collection 接口被扩展，提供了两个获取流的方法：

* public default Stream<E> stream() : 返回一个顺序流

* public default Stream<E> parallelStream() : 返回一个并行流

**2、创建 Stream方式二：通过数组**

Java8 中的 Arrays 的静态方法 stream() 可以获取数组流：

* public static <T> Stream<T> stream(T[] array): 返回一个流

重载形式，能够处理对应基本类型的数组：

* public static IntStream stream(int[] array)：返回一个整型数据流
* public static LongStream stream(long[] array)：返回一个长整型数据流
* public static DoubleStream stream(double[] array)：返回一个浮点型数据流

**3、创建 Stream方式三：通过Stream的of()**

可以调用Stream类静态方法 of(), 通过显示值创建一个流。它可以接收任意数量的参数。

* public static<T> Stream<T> of(T... values) : 返回一个顺序流

**4、创建 Stream方式四：创建无限流**

可以使用静态方法 Stream.iterate() 和 Stream.generate(), 创建无限流。

* public static<T> Stream<T> iterate(final T seed, final UnaryOperator<T> f):返回一个无限流
* public static<T> Stream<T> generate(Supplier<T> s) ：返回一个无限流

### 11.2.2 Stream中间操作API

多个中间操作可以连接起来形成一个流水线，除非流水线上触发终止操作，否则中间操作不会执行任何的处理！而在终止操作时一次性全部处理，称为“惰性求值”。

| 序号 | **方  法**                             | **描  述**                                                   |
| ---- | -------------------------------------- | ------------------------------------------------------------ |
| 1    | Stream filter(Predicate p)             | 接收 Lambda ， 从流中排除某些元素                            |
| 2    | Stream distinct()                      | 筛选，通过流所生成元素的equals() 去除重复元素                |
| 3    | Stream limit(long maxSize)             | 截断流，使其元素不超过给定数量                               |
| 4    | Stream skip(long n)                    | 跳过元素，返回一个扔掉了前 n 个元素的流。若流中元素不足 n 个，则返回一个空流。与 limit(n) 互补 |
| 5    | Stream peek(Consumer action)           | 接收Lambda，对流中的每个数据执行Lambda体操作                 |
| 6    | Stream sorted()                        | 产生一个新流，其中按自然顺序排序                             |
| 7    | Stream sorted(Comparator com)          | 产生一个新流，其中按比较器顺序排序                           |
| 8    | Stream map(Function f)                 | 接收一个函数作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素。 |
| 9    | Stream mapToDouble(ToDoubleFunction f) | 接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 DoubleStream。 |
| 10   | Stream mapToInt(ToIntFunction f)       | 接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 IntStream。 |
| 11   | Stream  mapToLong(ToLongFunction f)    | 接收一个函数作为参数，该函数会被应用到每个元素上，产生一个新的 LongStream。 |
| 12   | Stream flatMap(Function f)             | 接收一个函数作为参数，将流中的每个值都换成另一个流，然后把所有流连接成一个流 |

### 11.2.3 终结Stream操作API

终端操作会从流的流水线生成结果。其结果可以是任何不是流的值，例如：List、Integer，甚至是 void。流进行了终止操作后，不能再次使用。

| 序号 | 方法的返回值类型 | **方法**                             | **描述**                                                     |
| ---- | ---------------- | ------------------------------------ | ------------------------------------------------------------ |
| 1    | boolean          | **allMatch(Predicate p)**            | 检查是否匹配所有元素                                         |
| 2    | boolean          | **anyMatch**(**Predicate p**)        | 检查是否至少匹配一个元素                                     |
| 3    | boolean          | **noneMatch(Predicate  p)**          | 检查是否没有匹配所有元素                                     |
| 4    | Optional<T>      | **findFirst()**                      | 返回第一个元素                                               |
| 5    | Optional<T>      | **findAny()**                        | 返回当前流中的任意元素                                       |
| 6    | long             | **count()**                          | 返回流中元素总数                                             |
| 7    | Optional<T>      | **max(Comparator c)**                | 返回流中最大值                                               |
| 8    | Optional<T>      | **min(Comparator c)**                | 返回流中最小值                                               |
| 9    | void             | **forEach(Consumer c)**              | 迭代                                                         |
| 10   | T                | **reduce(T iden, BinaryOperator b)** | 可以将流中元素反复结合起来，得到一个值。返回 T               |
| 11   | U                | **reduce(BinaryOperator b)**         | 可以将流中元素反复结合起来，得到一个值。返回 Optional<T>     |
| 12   | List<T>          | toList()                             | JDK16引入的，将流中元素收集到List集合中                      |
| 13   | Object[]         | toArray()                            | JDK16引入的，将流中元素收集到Object数组中                    |
| 14   | R                | **collect(Collector c)**             | 将流转换为其他形式。接收一个 Collector接口的实现，用于给Stream中元素做汇总的方法 |

Collector 接口中方法的实现决定了如何对流执行收集的操作(如收集到 List、Set、Map)。Collector对象由Collectors工具的静态方法来创建。

### 11.2.4 java.util.stream.Collectors

Collectors 工具类提供了很多静态方法，可以方便地创建常见收集器实例。

| 序号 | 方法                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | static <T> Collector<T,?,List<T>> toList()                   | 返回一个Collector，用于将流中的数据收集到一个List集合中      |
| 2    | static <T> Collector<T,?,Set<T>> toSet()                     | 返回一个Collector，用于将流中的数据收集到一个Set集合中       |
| 3    | static <T,K,U> Collector<T,?,Map<K,U>> toMap(Function<? super T,? extends K> keyMapper, Function<? super T,? extends U> valueMapper) | 返回一个Collector，用于将流中的数据收集到一个Map集合中       |
|      |                                                              |                                                              |
| 4    | static <T> Collector<T,?,Optional<T>> reducing(BinaryOperator<T> op) | 基于op指定的操作对流中的数据进行归纳，最终得到一个对象结果   |
| 5    | static <T> Collector<T,?,T> reducing(T identity, BinaryOperator<T> op) | 基于op指定的操作对流中的数据进行归纳，最终得到一个对象结果，起始值是identity |
|      |                                                              |                                                              |
| 6    | static <T> Collector<T,?,Double> averagingDouble(ToDoubleFunction<? super T> mapper) | 返回一个 Collector ，用于将其他类型的对象流转换为double流，然后求它们的平均值。 |
| 7    | static <T> Collector<T,?,Double> averagingInt(ToIntFunction<? super T> mapper) | 返回一个 Collector ，用于将其他类型的对象流转换为int流，然后求它们的平均值。 |
| 8    | static <T> Collector<T,?,Double> averagingLong(ToLongFunction<? super T> mapper) | 返回一个 Collector ，用于将其他类型的对象流转换为long流，然后求它们的平均值。 |
|      |                                                              |                                                              |
| 9    | static <T> Collector<T,?,Long> counting()                    | 返回一个 Collector ，用于统计流中元素的数量                  |
|      |                                                              |                                                              |
| 10   | static <T> Collector<T,?,Optional<T>> maxBy(Comparator<? super T> comparator) | 返回一个Collector，用于对流中的数据基于定制比较器comparator查找最大值 |
| 11   | static <T> Collector<T,?,Optional<T>> minBy(Comparator<? super T> comparator) | 返回一个Collector，用于对流中的数据基于定制比较器comparato查找最小值 |
|      |                                                              |                                                              |
| 12   | static <T> Collector<T,?,Double> summingDouble(ToDoubleFunction<? super T> mapper) | 返回一个Collector，用于将其他类型的对象流转换为double流，然后求它们的总和。 |
| 13   | static <T> Collector<T,?,Integer> summingInt(ToIntFunction<? super T> mapper) | 返回一个Collector，用于将其他类型的对象流转换为int流，然后求它们的总和。 |
| 14   | static <T> Collector<T,?,Long> summingLong(ToLongFunction<? super T> mapper) | 返回一个Collector，用于将其他类型的对象流转换为long流，然后求它们的总和。 |
|      |                                                              |                                                              |
| 15   | static <T> Collector<T,?,DoubleSummaryStatistics> summarizingDouble(ToDoubleFunction<? super T> mapper) | 返回一个Collector，用于将其他类型的对象流转换为double流，然后求它们的总和、平均值、最大最小值、总数量。 |
| 16   | static <T> Collector<T,?,IntSummaryStatistics> summarizingInt(ToIntFunction<? super T> mapper) | 返回一个Collector，用于将其他类型的对象流转换为int流，然后求它们的总和、平均值、最大最小值、总数量。 |
| 17   | static <T> Collector<T,?,LongSummaryStatistics> summarizingLong(ToLongFunction<? super T> mapper) | 返回一个Collector，用于将其他类型的对象流转换为long流，然后求它们的总和、平均值、最大最小值、总数量。 |
|      |                                                              |                                                              |
| 18   | static <T,K> Collector<T,?,Map<K,List<T>>> groupingBy(Function<? super T,? extends K> classifier) | 返回一个Collector，用于对流中的数据进行分组统计              |
| 19   | static <T,K,A,D> Collector<T,?,Map<K,D>> groupingBy(Function<? super T,? extends K> classifier, Collector<? super T,A,D> downstream) | 返回一个Collector，用于对流中的数据进行分组统计，然后基于分组再对流中的数据使用downstream进行统计 |
| 20   | static <T> Collector<T,?,Map<Boolean,List<T>>> partitioningBy(Predicate<? super T> predicate) | 返回一个Collector，用于对流中的数据进行分组统计，结果是Map<Boolean, List<T>> |
| 21   | static <T,D,A> Collector<T,?,Map<Boolean,D>> partitioningBy(Predicate<? super T> predicate, Collector<? super T,A,D> downstream) | 返回一个Collector，用于对流中的数据进行分组统计，然后基于分组结果Map<Boolean, List<T>>再对流中的数据使用downstream进行统计 |

## 11.3、java.util.Optional类

Optional实际上是个容器：它可以保存类型T的值，或者仅仅保存null。Optional提供很多有用的方法，这样我们就不用显式进行空值检测。

| 序号 | 构造器或方法                                                 | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | static <T> Optional<T> empty()                               | 用来创建一个空的Optional                                     |
| 2    | static <T> Optional<T> of(T value)                           | 用来创建一个非空的Optional                                   |
| 3    | static <T> Optional<T> ofNullable(T value)                   | 用来创建一个可能是空，也可能非空的Optional                   |
|      |                                                              |                                                              |
| 4    | T get()                                                      | 返回Optional容器中的对象。要求Optional容器必须非空。T get()与of(T value)使用是安全的 |
| 5    | T orElse(T other)                                            | 如果Optional容器中非空，就返回所包装值，如果为空，就用orElse(T other)other指定的默认值（备胎）代替。一般orElse(T other) 与ofNullable(T value)配合使用 |
| 6    | T orElseGet(Supplier<? extends T> other)                     | 如果Optional容器中非空，就返回所包装值，如果为空，就用Supplier接口的Lambda表达式提供的值代替 |
| 7    | <X extends Throwable> T orElseThrow(Supplier<? extends X> exceptionSupplier) | 如果Optional容器中非空，就返回所包装值，如果为空，就抛出你指定的异常类型代替原来的NoSuchElementException |
|      |                                                              |                                                              |
| 8    | boolean isPresent()                                          | 判断Optional容器中的值是否存在                               |
| 9    | void ifPresent(Consumer<? super T> consumer)                 | 判断Optional容器中的值是否存在，如果存在，就对它进行Consumer指定的操作，如果不存在就不做 |
| 10   | <U> Optional<U> map(Function<? super T,? extends U> mapper)  | 判断Optional容器中的值是否存在，如果存在，就对它进行Function接口指定的操作，如果不存在就不做 |



# 十二、多线程

## 12.1 java.lang.Runnable接口

公共的抽象方法：

void run()：线程要完成的任务代码需要写到run方法中。

## 12.2 java.lang.Thread类

### 12.2.1 构造器

- public Thread() :分配一个新的线程对象。
- public Thread(String name) :分配一个指定名字的新线程对象。
- public Thread(Runnable target) :分配一个带有指定目标新的线程对象。
- public Thread(Runnable target,String name) :分配一个带有指定目标新的线程对象并指定名字。

###  12.2.2 常用方法

* public void run() :此线程要执行的任务在此处定义代码。

* public void start() :导致此线程开始执行; Java虚拟机调用此线程的run方法。

* public ==static== Thread currentThread() :返回当前正在执行这句语句的线程对象的引用。

* public String getName() :获取当前线程名称。默认是Thread-0，Thread-1，。。。。

* public void setName(String name)：设置线程名称。

* public final boolean isAlive()：测试线程是否处于活动状态。如果线程已经启动且尚未终止，则为活动状态。 

* public final int getPriority() ：返回线程优先级 

* public final void setPriority(int newPriority) ：改变线程的优先级

  * 每个线程都有一定的优先级，优先级高的线程将获得较多的执行机会。每个线程默认的优先级都与创建它的父线程具有相同的优先级。Thread类提供了setPriority(int newPriority)和getPriority()方法类设置和获取线程的优先级，其中setPriority方法需要一个整数，并且范围在[1,10]之间，通常推荐设置Thread类的三个优先级常量：
  * MAX_PRIORITY（10）：最高优先级 
  * MIN _PRIORITY （1）：最低优先级
  * NORM_PRIORITY （5）：普通优先级，默认情况下main线程具有普通优先级。

* public ==static== void sleep(long millis) :使当前正在执行的线程以指定的毫秒数暂停（暂时停止执行）。

* public ==static== void yield()：yield只是让当前线程暂停一下，让系统的线程调度器重新调度一次，希望优先级与当前线程相同或更高的其他线程能够获得执行机会，但是这个不能保证，完全有可能的情况是，当某个线程调用了yield方法暂停之后，线程调度器又将其调度出来重新执行。

* void join() ：等待该线程终止。 

  void join(long millis) ：等待该线程终止的时间最长为 millis 毫秒。如果millis时间到，将不再等待。 

  void join(long millis, int nanos) ：等待该线程终止的时间最长为 millis 毫秒 + nanos 纳秒。 

- public void interrupt()：中断线程。要通过这个方法制造InterrupttedException异常的话，前提是这个线程正在执行可能发生该异常的方法，例如：sleep，wait等。

- public final void stop()：强迫线程停止执行。 该方法具有固有的不安全性，已经标记为@Deprecated==（已过时、已废弃）==不建议再使用，那么我们就需要通过其他方式来停止线程了，其中一种方式是使用变量的值的变化来控制线程是否结束。

- public void setDaemon(true)：将指定线程设置为守护线程。必须在线程启动之前设置，否则会报IllegalThreadStateException异常。


- public boolean isDaemon()：判断线程是否是守护线程。

# 十三、文件目录和IO流

## 13.1 java.io.File类

### 1、构造器

在API中File的解释是文件和目录路径名的抽象表示形式，即要表示某个文件或者目录必须指定文件或目录的路径名称，如：d:/atguigu/javase/io/佟刚.jpg，d:/atguigu，http://www.atguigu.com/index.jsp。

| 序号 | 方法                                     | 描述                                                         |
| ---- | ---------------------------------------- | ------------------------------------------------------------ |
| 1    | public File(String pathname)             | 通过将给定的**路径名字符串**转换为抽象路径名来创建新的 File实例。 |
| 2    | public File(String parent, String child) | 从**父路径名字符串和子路径名字符串**创建新的 File实例。      |
| 3    | public File(File parent, String child)   | 从**父抽象路径名和子路径名字符串**创建新的 File实例。        |

### 2、获取文件和目录基本信息的方法

| 序号 | 方法                         | 描述                                                         |
| ---- | ---------------------------- | ------------------------------------------------------------ |
| 1    | public String getName()      | 返回由此File表示的文件或目录的名称。                         |
| 2    | public long length()         | 返回由此File表示的文件的长度。 如果此路径名表示一个目录，则返回值是不确定的。 |
| 3    | public long lastModified()   | 返回File对象对应的文件或目录的最后修改时间（毫秒值）。       |
| 4    | public boolean exists()      | 此File表示的文件或目录是否实际存在。                         |
| 5    | public boolean isDirectory() | 此File表示的是否为目录。                                     |
| 6    | public boolean isFile()      | 此File表示的是否为文件。                                     |
| 7    | public boolean isHidden()    | 此File表示的是否为隐藏文件或目录。                           |
| 8    | public boolean canExecute()  | 测试应用程序是否可以执行此抽象路径名表示的文件。             |
| 9    | public boolean canRead()     | 测试应用程序是否可以读取此抽象路径名表示的文件。             |
| 10   | public boolean canWrite()    | 测试应用程序是否可以修改此抽象路径名表示的文件。             |

### 3、创建删除文件和目录

| 序号 | 方法                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | public static File **createTempFile**(String prefix,                                   String suffix)                            throws IOException | 在默认临时文件目录中创建一个空文件，使用给定前缀和后缀生成其名称。 |
| 2    | public static File **createTempFile**(String prefix,                                   String suffix,                                   File directory)                            throws IOException | 在指定目录中创建一个新的空文件，使用给定的前缀和后缀字符串生成其名称。 |
| 3    | public boolean **createNewFile**()                           | 当且仅当具有该名称的文件尚不存在时，创建一个新的空文件。     |
| 4    | public boolean **delete**()                                  | 删除由此File表示的文件或==空==目录。                         |
| 5    | public boolean mkdir()                                       | 创建由此File表示的目录。                                     |
| 6    | public boolean mkdirs()                                      | 创建由此File表示的目录，包括任何必需但不存在的父目录。       |
| 7    | public boolean renameTo(File dest)                           | 重新命名此抽象路径名表示的文件或目录。但是此方法行为的许多方面都是与平台有关的：重命名操作无法将一个文件从一个文件系统移动到另一个文件系统。 |

### 4、文件或目录的上下级

| 序号 | 方法                                           | 描述                                                         |
| ---- | ---------------------------------------------- | ------------------------------------------------------------ |
| 1    | public String getParent()                      | 返回此抽象路径名父目录的路径名字符串                         |
| 2    | public File getParentFile()                    | 返回此抽象路径名父目录的抽象路径名                           |
| 3    | public String[] list()                         | 返回一个String数组，表示该File目录中的所有子文件或目录。     |
| 4    | public File[] listFiles()                      | 返回一个File数组，表示该File目录中的所有的子文件或目录。     |
| 5    | public File[] listFiles(FileFilter filter)     | 返回所有满足指定过滤器的文件和目录。如果给定 filter 为 null，则接受所有路径名。否则，当且仅当在路径名上调用过滤器的 FileFilter.accept(File pathname)方法返回 true 时，该路径名才满足过滤器。 |
| 6    | public String[] list(FilenameFilter filter)    | 返回返回所有满足指定过滤器的文件和目录。如果给定 filter 为 null，则接受所有路径名。否则，当且仅当在路径名上调用过滤器的 FilenameFilter .accept(File dir, String name)方法返回 true 时，该路径名才满足过滤器。 |
| 7    | public File[] listFiles(FilenameFilter filter) | 返回返回所有满足指定过滤器的文件和目录。如果给定 filter 为 null，则接受所有路径名。否则，当且仅当在路径名上调用过滤器的 FilenameFilter .accept(File dir, String name)方法返回 true 时，该路径名才满足过滤器。 |

### 5、各种路径问题

| 序号 | 方法                            | 描述                               |
| ---- | ------------------------------- | ---------------------------------- |
| 1    | public String getPath()         | 将此File转换为路径名字符串。       |
| 2    | public String getAbsolutePath() | 返回此File的绝对路径名字符串。     |
| 3    | String getCanonicalPath()       | 返回此File对象所对应的规范路径名。 |

（1）绝对路径：

- windows：从盘符开始的路径，就是绝对路径，例如：D:\download\学生项目
- linux：从/符号开始的路径，就是绝对路径

（2）相对路径：

- 除了绝对路径，就是相对路径。
- 相对谁？JavaSE项目
  - main方法中代码：参考project（工程，项目）
  - @Test方法中代码：参考module（模块）

（3）构造路径：new File对象时，指定的path，它可能是相对路径，也可能是绝对路径，可能是规范路径，也可以是非规范路径。

（4）规范路径：不包含../等形式的路径值。

## 13.2 java.io.FileFilter

抽象路径名的过滤器。 

- public boolean accept(File pathname) 判断指定的抽象路径名是否应包含在路径名列表中。

## 13.3 IO流

### 13.3.1 IO流分类

#### 按照继承关系分

| 分类       | 父类         | 子类                 | 描述                                                         |
| ---------- | ------------ | -------------------- | ------------------------------------------------------------ |
| 字节输入流 | InputStream  | FileInputStream      | 以字节为单位的方式读取任意类型的文件内容                     |
|            |              | BufferedInputStream  | 包装其他InputStream流，先将其他InputStream流读取字节内容预先缓存到缓冲区，之后再从缓冲区中读取数据 |
|            |              | DataInputStream      | 包装其他InputStream流，并按照不同数据类型从该流中读取数据    |
|            |              | ObjectInputStream    | 包装其他InputStream流，并按照不同数据类型从该流中读取数据，并支持对象反序列化 |
| 字节输出流 | OutputStream | FileOutputStream     | 以字节为单位的方式输出内容至任意类型的文件                   |
|            |              | BufferedOutputStream | 包装其他OutputStream流，先将数据先输出到缓冲区，之后再从缓冲区输出到所包装的输出流中 |
|            |              | DataOutputStream     | 包装其他OutputStream流，先按照不同数据类型将数据输出到该输出流，之后再从该流以字节方式输出到所包装的输出流中 |
|            |              | ObjectOutputStream   | 包装其他OutputStream流，先按照不同数据类型将数据输出到该输出流，之后再从该流以字节方式输出到所包装的输出流中，并支持对象的序列化 |
|            |              | PrintStream          | 将流中数据打印输出到文件或另一个OutputStream流中             |
| 字符输入流 | Reader       | FileReader           | 以字符为单位的方式读取纯文本文件的内容                       |
|            |              | BufferedReader       | 包装其他Reader类，先将其他Reader流读取字符内容预先缓存到缓冲区，之后再从缓冲区中读取数据 |
|            |              | InputStreamReader    | 包装其他InputStream类，将所包装的InputStream流中的字节数据解码为字符 |
| 字符输出流 | Writer       | FileWriter           | 以字符为单位的方式输出内容至纯文本文件                       |
|            |              | BufferedWriter       | 包装其他Writer流，先将数据先输出到缓冲区，之后再从缓冲区输出到所包装的输出流中 |
|            |              | OutputStreamWriter   | 包装其他OutputStream类，将字符数据编码为字节数据输出到所包装的OutputStream流中 |
|            |              | PrinterWriter        | 将流中数据打印输出到文件或另一个Writer流中                   |

#### 按照功能划分

| 功能     | IO流                 | 描述                                                         |
| -------- | -------------------- | ------------------------------------------------------------ |
| 读写文件 | FileInputStream      | 以字节为单位的方式读取任意类型的文件内容                     |
|          | FileOutputStream     | 以字节为单位的方式输出内容至任意类型的文件                   |
|          | FileReader           | 以字符为单位的方式读取纯文本文件的内容                       |
|          | FileWriter           | 以字符为单位的方式输出内容至纯文本文件                       |
| 打印流   | PrintStream          | 将流中数据打印输出到文件或另一个OutputStream流中             |
|          | PrintWriter          | 将流中数据打印输出到文件或另一个OutputStream流中             |
| 转换流   | InputStreamReader    | 包装其他InputStream类，将所包装的InputStream流中的字节数据解码为字符 |
|          | OutputStreamWriter   | 包装其他OutputStream类，将字符数据编码为字节数据输出到所包装的OutputStream流中 |
| 缓冲流   | BufferedInputStream  | 包装其他InputStream流，先将其他InputStream流读取字节内容预先缓存到缓冲区，之后再从缓冲区中读取数据 |
|          | BufferedOutputStream | 包装其他OutputStream流，先将数据先输出到缓冲区，之后再从缓冲区输出到所包装的输出流中 |
|          | BufferedReader       | 包装其他Reader类，先将其他Reader流读取字符内容预先缓存到缓冲区，之后再从缓冲区中读取数据 |
|          | BufferedWrtier       | 包装其他Writer流，先将数据先输出到缓冲区，之后再从缓冲区输出到所包装的输出流中 |
| 数据流   | DataInputStream      | 包装其他InputStream流，并按照不同数据类型从该流中读取数据    |
|          | DataOutputStream     | 包装其他OutputStream流，先按照不同数据类型将数据输出到该输出流，之后再从该流以字节方式输出到所包装的输出流中 |
| 对象流   | ObjectInputStream    | 包装其他InputStream流，并按照不同数据类型从该流中读取数据，并支持对象反序列化 |
|          | ObjectOutputStream   | 包装其他OutputStream流，先按照不同数据类型将数据输出到该输出流，之后再从该流以字节方式输出到所包装的输出流中，并支持对象的序列化 |



### 13.3.1 java.io.InputStream

- public int read()：一次读取1个字节，返回的该字节值。如果流中已经没有数据可读了，返回-1。
- public int read(byte[] data)：一次读取多个字节，返回的本次读取的字节个数。最多可以读取data.length个，如果流中不够data.length个，有几个字节读取几个。如果流中已经没有数据可读了，返回-1。读取的内容放入data字节数组[0, n)下标范围，n为本次读取的字节数量。
- public int read(byte[] b, int off, int len)：一次读取多个字节，返回的本次读取的字节个数。最多可以读取len个，如果流中不够len个，有几个字节读取几个。如果流中已经没有数据可读了，返回-1。读取的内容放入data字节数组[0, n)下标范围，n为本次读取的字节数量。
- public void close()：关闭IO流。



### 13.3.2 java.io.OutputStream

- public void writer(int n)：输出1个字节
- public void write(byte [] data)：输出整个字节数组中内容
- public void write(byte [] data,int offset, int len)：输出字节数组中一部分内容。从data的[offset]开始取len个字节。
- public void close()：关闭IO流。
- public void flush()：刷新IO流。



### 13.3.3 java.io.Reader

- public int read()：一次读取1个字符，返回的该字符的Unicode编码值。如果流中已经没有数据可读了，返回-1。
- public int read(char[] data)：一次读取多个字符，返回的本次读取的字符个数。最多可以读取data.length个，如果流中不够data.length个，有几个字符读取几个。如果流中已经没有数据可读了，返回-1。
- public int read(char[] data, int off, int len)：一次读取多个字符，返回的本次读取的字符个数。最多可以读取len个，如果流中不够len个，有几个字符读取几个。如果流中已经没有数据可读了，返回-1。读取的内容放入data字符数组[0, n)下标范围，n为本次读取的字符数量。
- public void close()：关闭IO流。

### 13.3.4 java.io.Writer

- public void write(int ch)：输出1个字符
- public void write(String str)：输出整个字符串
- public void write(char[] data)：输出整个char数组
- public void write(char[] data, int offset, int len)：输出char数组的一部分。从data数组的[offset]开始取len个字符输出。
- public void write(String str, int offset, int ln)：输出字符串的一部分。从str字符串的[offset]开始取len个字符输出。
- public void close()：关闭IO流。
- public void flush()：刷新IO流。

### 13.3.5 java.io.FileReader

- public FileReader(File file)：创建FileReader对象，从file文件读取内容
- public FileReader(String fileName)：创建FileReader对象，从fileName指定的文件读取文件内容
- public FileReader(File file, Charset charset)：创建FileReader对象，从file文件读取内容，文件编码是charset
- public FileReader(String fileName, Charset charset)创建FileReader对象，从fileName指定的文件读取文件内容，文件编码是charset

### 13.3.6 java.io.FileWriter

- public FileWriter(File file)：创建FileWriter对象，将内容写到file文件。如果文件已存在，会覆盖原文件
- public FileWriter(String fileName)：创建FileWriter对象，将内容写到fileName指定的文件，如果文件已存在，会覆盖原文件
- public FileWriter(File file, boolean append)：创建FileWriter对象，将内容写到file文件。如果文件已存在，会进行续写。
- public FileWriter(String fileName, boolean append)：创建FileWriter对象，将内容写到fileName指定的文件，如果文件已存在，会进行续写。
- public FileWriter(File file, Charset charset)：创建FileWriter对象，将内容写到file文件。文件编码是charset。如果文件已存在，会覆盖原文件
- public FileWriter(String fileName, Charset charset)：创建FileWriter对象，将内容写到fileName指定的文件，文件编码是charset。如果文件已存在，会覆盖原文件。
- public FileWriter(File file, Charset charset, boolean append)：创建FileWriter对象，将内容写到file文件。文件编码是charset。如果文件已存在，会进行续写。
- public FileWriter(String fileName, Charset charset, boolean append)：创建FileWriter对象，将内容写到fileName指定的文件，文件编码是charset。如果文件已存在，会进行续写。

### 13.3.7 java.io.ObjectOutputStream

ObjectOutputStream必须包装一个OutputStream字节输出流对象。

- public ObjectOutputStream(OutputStream out)：创建一个写入指定的OutputStream的ObjectOutputStream。

ObjectOutputStream是OutputStream的子类，==除了OutputStream的方法==，还增加了一些方法：

| 序号 | 方法                                       | 描述              |
| ---- | ------------------------------------------ | ----------------- |
| 1    | public void writeBoolean(boolean val)      | 输出一个boolean值 |
| 2    | public void writeByte(int val)             | 输出一个byte值    |
| 3    | public void writeShort(int val)            | 输出一个short值   |
| 4    | public void writeChar(int val)             | 输出一个char值    |
| 5    | public void writeInt(int val)              | 输出一个int值     |
| 6    | public void writeLong(long val)            | 输出一个long值    |
| 7    | public void writeFloat(float val)          | 输出一个float值   |
| 8    | public void writeDouble(double val)        | 输出一个double值  |
| 9    | public void writeUTF(String str)           | 输出一个String值  |
|      |                                            |                   |
| 10   | public final void writeObject (Object obj) | 输出一个对象      |

### 13.3.8 java.io.ObjectInputStream

ObjectInputStream必须包装一个InputStream字节输入流对象。

- ObjectInputStream(InputStream in)：创建从指定的InputStream读取的ObjectInputStream。 

ObjectInputStream是InputStream的子类，除了InputStream的方法，还增加了一些方法：

ObjectOutputStream是OutputStream的子类，==除了OutputStream的方法==，还新增了如下方法：

| 序号 | 方法                              | 描述              |
| ---- | --------------------------------- | ----------------- |
| 1    | public boolean readBoolean()      | 读取一个boolean值 |
| 2    | public byte readByte()            | 读取一个byte值    |
| 3    | public short readShort()          | 读取一个short值   |
| 4    | public char readChar()            | 读取一个char值    |
| 5    | public int readInt()              | 读取一个int值     |
| 6    | public long readLong()            | 读取一个long值    |
| 7    | public float readFloat()          | 读取一个float值   |
| 8    | public double readDouble()        | 读取一个double值  |
| 9    | public String readUTF()           | 读取一个String值  |
|      |                                   |                   |
| 10   | public final Object readObject () | 读取一个对象      |

### 13.3.9 java.io.PrintStream

- PrintStream(File file)：使用指定的文件创建一个新的打印流，而不需要自动换行。 

- PrintStream(File file, String csn)：使用指定的文件和字符集创建新的打印流，而不需要自动换行。

- PrintStream(OutputStream out)：创建一个新的打印流。  

- PrintStream(OutputStream out, boolean autoFlush)：创建一个新的打印流。  

- PrintStream(OutputStream out, boolean autoFlush, String encoding)：创建一个新的打印流。 

- PrintStream(String fileName)：使用指定的文件名创建新的打印流，不需要自动换行。  

- PrintStream(String fileName, String csn)：创建一个新的打印流，不需要自动换行，具有指定的文件名和字符集。

PrintStream流是OutputStream流的子类，==除了OutputStream的方法==，还新增了如下方法：

| 序号 | 方法                           | 描述                                             |
| ---- | ------------------------------ | ------------------------------------------------ |
| 1    | public void print(boolean b)   | 打印输出一个boolean值                            |
| 2    | public void print(char b)      | 打印输出一个char值                               |
| 3    | public void print(char[] b)    | 打印输出一个char[]                               |
| 4    | public void print(double b)    | 打印输出一个double值                             |
| 5    | public void print(float b)     | 打印输出一个float值                              |
| 6    | public void print(int b)       | 打印输出一个int值                                |
| 7    | public void print(long b)      | 打印输出一个long值                               |
| 8    | public void print(Object b)    | 打印输出一个对象，自动调用对象toString方法       |
| 9    | public void print(String b)    | 打印输出一个字符串                               |
|      |                                |                                                  |
| 10   | public void println()          | 打印输出一个换行符                               |
| 1    | public void println(boolean b) | 打印输出一个boolean值并换行                      |
| 2    | public void println(char b)    | 打印输出一个char值并换行                         |
| 3    | public void println(char[] b)  | 打印输出一个char[]并换行                         |
| 4    | public void println(double b)  | 打印输出一个double值并换行                       |
| 5    | public void println(float b)   | 打印输出一个float值并换行                        |
| 6    | public void println(int b)     | 打印输出一个int值并换行                          |
| 7    | public void println(long b)    | 打印输出一个long值并换行                         |
| 8    | public void println(Object b)  | 打印输出一个对象并换行，自动调用对象toString方法 |
| 9    | public void println(String b)  | 打印输出一个字符串并换行                         |

### 13.3.10 java.util.Scanner

- public Scanner(File source)：创建Scanner对象，从source文件读取内容
- public Scanner(File source, String charsetName)：创建Scanner对象，从source文件读取内容。文件编码是charsetName。
- public Scanner(File source, Charset charset)：创建Scanner对象，从source文件读取内容。文件编码是charset。
- public Scanner(InputStream source)：创建Scanner对象，从source输入流读取内容。
- public Scanner(InputStream source, String charsetName)：创建Scanner对象，从source输入流读取内容。流中文本编码是charsetName
- public Scanner(InputStream source, Charset charset)：创建Scanner对象，从source输入流读取内容。流中文本编码是charset



常用方法：

| 序号 | 方法                               | 描述                                                         | 方法                                    | 描述                           |
| ---- | ---------------------------------- | ------------------------------------------------------------ | --------------------------------------- | ------------------------------ |
| 1    | public boolean hasNextByte()       | 当且仅当此扫描器的下一个标记是有效的字节值时才返回 true      | public byte nextByte()                  | 读取1个字节                    |
| 2    | public boolean hasNextShort()      | 当且仅当此扫描器的下一个标记是默认基数中的有效的 short 值时才返回 true | public short nextShort()                | 读取一个boolean值              |
| 3    | public boolean hasNextInt()        | 当且仅当此扫描器的下一个标记是有效的 int 值时才返回 true     | public int nextInt()                    | 读取一个int值                  |
| 4    | public boolean hasNextLong()       | 当且仅当此扫描器的下一个标记是有效的 long 值时才返回 true    | 将输入信息的下一个标记扫描为一个 long。 | 读取一个long值                 |
| 5    | public boolean hasNextFloat()      | 当且仅当此扫描器的下一个标记是有效的 float 值时才返回 true   | public float nextFloat()                | 读取一个float值                |
| 6    | public boolean hasNextDouble()     | 当且仅当此扫描器的下一个标记是有效的 double 值时才返回 true  | public double nextDouble()              | 读取一个double值               |
| 7    | public boolean hasNextBigInteger() | 当且仅当此扫描器的下一个标记是有效的 BigInteger 值时才返回 true | public BigInteger nextBigInteger()      | 读取一个BigInteger值           |
| 8    | public boolean hasNextBigDecimal() | 当且仅当此扫描器的下一个标记是有效的 BigDecimal 值时才返回 true | public BigDecimal nextBigDecimal()      | 读取一个BigDecimal值           |
| 9    | public boolean hasNext()           | 如果此扫描器的输入中有另一个标记，则返回 true。在等待要扫描的输入时，此方法可能阻塞。 | public String next()                    | 读取一个字符串，遇到空格结束   |
| 10   | public boolean hasNextLine()       | 当且仅当此扫描器有另一行输入时才返回 true                    | public String nextLine()                | 读取一行字符串，遇到换行符结束 |





# 十四、网络编程

## 14.1 java.net.InetAddress

InetAddress类主要表示IP地址，两个子类：Inet4Address、Inet6Address。

Internet上的主机有两种方式表示地址：

* 域名(hostName)：www.atguigu.com
* IP 地址(hostAddress)：202.108.35.210

lInetAddress 类没有提供公共的构造器，而是提供 了 如下几个 静态方法来获取InetAddress 实例

* public static InetAddress getLocalHost()
* public static InetAddress getByName(String host)
* public static InetAddress getByAddress(byte[] addr)

InetAddress 提供了如下几个常用的方法

* public String getHostAddress() ：返回 IP 地址字符串（以文本表现形式）。
* public String getHostName() ：获取此 IP 地址的主机名

## 14.2 UDP协议

### 14.2.1 DatagramSocket 

此类表示用来发送和接收数据报包的套接字。数据报套接字是包投递服务的发送或接收点。每个在数据报套接字上发送或接收的包都是单独编址和路由的。从一台机器发送到另一台机器的多个包可能选择不同的路由，也可能按不同的顺序到达。 

| 序号 | 构造器或方法                          | 描述                                                         |
| ---- | ------------------------------------- | ------------------------------------------------------------ |
| 1    | public DatagramSocket(int port)       | 创建数据报套接字并将其绑定到本地主机上的指定端口。套接字将被绑定到通配符地址，IP 地址由内核来选择。 |
|      |                                       |                                                              |
| 2    | public void send(DatagramPacket p)    | 从此套接字发送数据报包。DatagramPacket 包含的信息指示：将要发送的数据、其长度、远程主机的 IP 地址和远程主机的端口号。 |
| 3    | public void receive(DatagramPacket p) | 从此套接字接收数据报包。当此方法返回时，DatagramPacket 的缓冲区填充了接收的数据。数据报包也包含发送方的 IP 地址和发送方机器上的端口号。 此方法在接收到数据报前一直阻塞。数据报包对象的 length 字段包含所接收信息的长度。如果信息比包的长度长，该信息将被截短。 |
|      |                                       |                                                              |
| 4    | public void close()                   | 关闭此数据报套接字。                                         |

### 14.2.2 DatagramPacket类

DatagramPacket此类表示数据报包。 数据报包用来实现无连接包投递服务。每条报文仅根据该包中包含的信息从一台机器路由到另一台机器。

| 序号 | 构造器和方法                                                 | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | public DatagramPacket(byte[] buf,int length)                 | 构造 DatagramPacket，用来接收长度为 length 的数据包。 length 参数必须小于等于 buf.length。 |
| 2    | public DatagramPacket(byte[] buf,int length,InetAddress address,int port) | 构造数据报包，用来将长度为 length 的包发送到指定主机上的指定端口号。length 参数必须小于等于 buf.length。 |
|      |                                                              |                                                              |
| 3    | public int getLength()                                       | 返回将要发送或接收到的数据的长度。                           |
| 4    | public byte[] getData()                                      | 返回数据缓冲区。                                             |

## 14.3 TCP协议

### 14.3.1 ServerSocket类

| 序号 | 构造器或方法           | 描述                               |
| ---- | ---------------------- | ---------------------------------- |
| 1    | ServerSocket(int port) | 创建绑定到特定端口的服务器套接字。 |
| 2    | Socket accept()        | 侦听并接受到此套接字的连接。       |
| 3    | public void close()    | 关闭此套接字。                     |

### 14.3.2 Socket类

| 序号 | 构造器或方法                                | 描述                                                         |
| ---- | ------------------------------------------- | ------------------------------------------------------------ |
| 1    | public Socket(InetAddress address,int port) | 创建一个流套接字并将其连接到指定 IP 地址的指定端口号。       |
| 2    | public Socket(String host,int port)         | 创建一个流套接字并将其连接到指定主机上的指定端口号。         |
|      |                                             |                                                              |
| 3    | public InputStream getInputStream()         | 返回此套接字的输入流，可以用于接收消息                       |
| 4    | public OutputStream getOutputStream()       | 返回此套接字的输出流，可以用于发送消息                       |
|      |                                             |                                                              |
| 5    | public InetAddress getInetAddress()         | 此套接字连接到的远程 IP 地址；如果套接字是未连接的，则返回 null。 |
| 6    | public int getPort()                        | 此套接字连接到的远程端口号；如果尚未连接套接字，则返回 0。   |
| 7    | public InetAddress getLocalAddress()        | 获取套接字绑定的本地地址。                                   |
| 8    | public int getLocalPort()                   | 返回此套接字绑定到的本地端口。如果尚未绑定套接字，则返回 -1。 |
|      |                                             |                                                              |
| 9    | public void close()                         | 关闭此套接字。套接字被关闭后，便不可在以后的网络连接中使用（即无法重新连接或重新绑定）。需要创建新的套接字对象。 关闭此套接字也将会关闭该套接字的 InputStream 和 OutputStream。 |
|      |                                             |                                                              |
| 10   | public void shutdownInput()                 | 如果在套接字上调用 shutdownInput() 后从套接字输入流读取内容，则流将返回 EOF（文件结束符）。 即不能在从此套接字的输入流中接收任何数据。 |
| 11   | public void shutdownOutput()                | 禁用此套接字的输出流。对于 TCP 套接字，任何以前写入的数据都将被发送，并且后跟 TCP 的正常连接终止序列。 如果在套接字上调用 shutdownOutput() 后写入套接字输出流，则该流将抛出 IOException。 即不能通过此套接字的输出流发送任何数据。 |

**注意：**先后调用Socket的shutdownInput()和shutdownOutput()方法，仅仅关闭了输入流和输出流，并不等于调用Socket的close()方法。在通信结束后，仍然要调用Scoket的close()方法，因为只有该方法才会释放Socket占用的资源，比如占用的本地端口号等。

# 十五、反射

## 15.1 获取Class对象的四种方式

（1）类型名.class：获取某类型的Class对象

```java
	@Test
    public void test1(){
        Class<?> c1 = int.class;

        Class<?> c2 = void.class;

        Class<?> c3 = String.class;
        Class<?> c4 = Serializable.class;
        Class<?> c5 = Month.class;
        Class<?> c6 = int[].class;
        Class<?> c7 = Override.class;

        //类型不同Class对象就不同
        //类型相同Class对象就相同
    }
```



（2）对象.getClass()：获取对象的运行时类型

```java
@Test
    public void test1(){
       Class c =  int.class;//int类型的字节码数据在内存中的Class对象
       Class s = String.class;//String类型的字节码数据在内存中的Class对象
        System.out.println(c == s);//false
    }

    @Test
    public void test2()throws Exception{
        Class c1 = "hello".getClass();//字符串类型
        Class c2 = String.class;//字符串类型
        System.out.println(c1 == c2);//true
        Class c3 = Class.forName("java.lang.String");
        System.out.println(c1 == c3);//true
    }
```



（3）Class.forName("类型全名称")：获取某类型的Class对象

 ```java
 Class c3 = Class.forName("java.lang.String");
 ```



（4）ClassLoader的类加载器对象.loadClass(类型全名称)：可以用系统类加载对象或自定义加载器对象加载指定路径下的类型

```java
Class c = ClassLoader.getSystemClassLoader().loadClass("java.lang.String");
```

## 15.2 相关类的API

### 1、java.lang.Class类

| 序号 | 方法                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | public static Class<?> **forName**(String className)throws ClassNotFoundException | 返回与带有给定字符串名的类或接口相关联的 Class 对象。        |
|      |                                                              |                                                              |
| 2    | public Package **getPackage**()                              | 获取此类的包。                                               |
| 3    | public int **getModifiers**()                                | 返回此类或接口以整数编码的 Java 语言修饰符。                 |
| 4    | public String **getName**()                                  | 以 String 的形式返回此 Class 对象所表示的实体（类、接口、数组类、基本类型或 void）名称。 |
|      |                                                              |                                                              |
| 5    | public Class<? super T> **getSuperclass**()                  | 返回表示此 Class 所表示的实体（类、接口、基本类型或 void）的超类的 Class。 |
| 6    | public Type **getGenericSuperclass**()                       | 回表示此 Class 所表示的实体（类、接口、基本类型或 void）的直接超类的 Type。如果超类是参数化类型，则返回的 Type 对象必须准确反映源代码中所使用的实际类型参数。 |
| 7    | public Class<?>[] **getInterfaces**()                        | 确定此对象所表示的类或接口实现的接口。如果此对象表示一个类，则返回值是一个数组，它包含了表示该类所实现的所有接口的对象。 |
| 8    | public Type[] **getGenericInterfaces**()                     | 返回表示某些接口的 Type，这些接口由此对象所表示的类或接口直接实现。 |
|      |                                                              |                                                              |
| 9    | public Field[] **getFields**()                   throws SecurityException | 返回一个包含某些 Field 对象的数组，这些对象反映此 Class 对象所表示的类或接口的所有可访问公共字段。返回数组中的元素没有排序，也没有任何特定的顺序。 |
| 10   | public Field **getField**(String name)                throws NoSuchFieldException,                       SecurityException | 返回一个 Field 对象，它反映此 Class 对象所表示的类或接口的指定公共成员字段。name 参数是一个 String，用于指定所需字段的简称。 |
| 11   | public Field[] **getDeclaredFields**()                           throws SecurityException | 返回 Field 对象的一个数组，这些对象反映此 Class 对象所表示的类或接口所声明的所有字段。包括公共、保护、默认（包）访问和私有字段，但不包括继承的字段。返回数组中的元素没有排序，也没有任何特定的顺序。 |
| 12   | public Field **getDeclaredField**(String name)                        throws NoSuchFieldException,                               SecurityException | 返回一个 Field 对象，该对象反映此 Class 对象所表示的类或接口的指定已声明字段。name 参数是一个 String，它指定所需字段的简称。 |
|      |                                                              |                                                              |
| 13   | public Constructor<?>[] **getConstructors**()                                  throws SecurityException | 返回一个包含某些 Constructor 对象的数组，这些对象反映此 Class 对象所表示的类的所有公共构造方法。 |
| 14   | public Constructor<T> **getConstructor**(Class<?>... parameterTypes)                               throws NoSuchMethodException,                                      SecurityException | 返回一个 Constructor 对象，它反映此 Class 对象所表示的类的指定公共构造方法。parameterTypes 参数是 Class 对象的一个数组，这些 Class 对象按声明顺序标识构造方法的形参类型。 如果此 Class 对象表示非静态上下文中声明的内部类，则形参类型作为第一个参数包括显示封闭的实例。 |
| 15   | public Constructor<?>[] **getDeclaredConstructors**()                                          throws SecurityException | 返回 Constructor 对象的一个数组，这些对象反映此 Class 对象表示的类声明的所有构造方法。它们是公共、保护、默认（包）访问和私有构造方法。 |
| 16   | public Constructor<T> **getDeclaredConstructor**(Class<?>... parameterTypes)                                       throws NoSuchMethodException,                                              SecurityException | 返回一个 Constructor 对象，该对象反映此 Class 对象所表示的类或接口的指定构造方法。parameterTypes 参数是 Class 对象的一个数组，它按声明顺序标识构造方法的形参类型。 如果此 Class 对象表示非静态上下文中声明的内部类，则形参类型作为第一个参数包括显示封闭的实例。 |
|      |                                                              |                                                              |
| 17   | public Method[] **getMethods**()                     throws SecurityException | 返回一个包含某些 Method 对象的数组，这些对象反映此 Class 对象所表示的类或接口（包括那些由该类或接口声明的以及从超类和超接口继承的那些的类或接口）的公共 member 方法。 |
| 18   | public Method **getMethod**(String name,                         Class<?>... parameterTypes)                  throws NoSuchMethodException,                         SecurityException | 返回一个 Method 对象，它反映此 Class 对象所表示的类或接口的指定公共成员方法。name 参数是一个 String，用于指定所需方法的简称。parameterTypes 参数是按声明顺序标识该方法形参类型的 Class 对象的一个数组。 |
| 19   | public Method[] **getDeclaredMethods**()                             throws SecurityException | 返回 Method 对象的一个数组，这些对象反映此 Class 对象表示的类或接口声明的所有方法，包括公共、保护、默认（包）访问和私有方法，但不包括继承的方法。返回数组中的元素没有排序，也没有任何特定的顺序。 |
| 20   | public Method **getDeclaredMethod**(String name,                                 Class<?>... parameterTypes)                          throws NoSuchMethodException,                                 SecurityException | 返回一个 Method 对象，该对象反映此 Class 对象所表示的类或接口的指定已声明方法。name 参数是一个 String，它指定所需方法的简称，parameterTypes 参数是 Class 对象的一个数组，它按声明顺序标识该方法的形参类型。 |
|      |                                                              |                                                              |
| 21   | public Class<?>[] **getClasses**()                           | 返回一个包含某些 Class 对象的数组，这些对象表示属于此 Class 对象所表示的类的成员的所有公共类和接口。（即内部类） |
| 22   | public Class<?>[] **getDeclaredClasses**()                               throws SecurityException | 返回 Class 对象的一个数组，这些对象反映声明为此 Class 对象所表示的类的成员的所有类和接口。包括该类所声明的公共、保护、默认（包）访问及私有类和接口，但不包括继承的类和接口。 |
| 23   | public Class<?> **getDeclaringClass**()                      | 如果此 Class 对象所表示的类或接口是另一个类的成员，则返回的 Class 对象表示该对象的声明类。如果该类或接口不是其他类的成员，则此方法返回 null。（即外部类） |
|      |                                                              |                                                              |
| 24   | public Annotation[] getAnnotations()                         | 返回此类型上存在的注解，包括从父类继承的注解。               |
| 25   | public Annotation[] getDeclaredAnnotations()                 | 返回直接存在于此类型上的注解，不包括从父类继承的注解。       |
| 26   | public <A extends Annotation> A getAnnotation(Class<A> annotationClass) | 返回此类型上的某个注解。                                     |
|      |                                                              |                                                              |
| 27   | public boolean **isAnonymousClass**()                        | 是否是匿名类                                                 |
| 28   | public boolean **isLocalClass**()                            | 是否是局部内部类                                             |
| 29   | public boolean **isMemberClass**()                           | 是否是成员内部类                                             |
| 30   | public boolean **isArray**()                                 | 是否是数组类型                                               |
| 31   | public boolean **isPrimitive**()                             | 是否是基本数据类型或void                                     |
| 32   | public boolean **isInterface**()                             | 是否是接口类型                                               |
| 33   | public boolean **isEnum**()                                  | 是否是枚举类型                                               |
| 34   | public boolean **isAnnotation**()                            | 是否是注解类型                                               |
|      |                                                              |                                                              |
| 35   | public T **newInstance**()               throws InstantiationException,                      IllegalAccessException | 创建此 Class 对象所表示的类的一个新实例。要求该类必须有一个公共的无参构造。此方法已过时。 |
|      |                                                              |                                                              |
| 36   | public ClassLoader **getClassLoader**()                      | 返回该类的类加载器。如果该类由引导类加载器加载，则此方法在这类实现中将返回 null。 |

### 2、java.lang.reflect.Modifier类

| 序号 | 常量或方法                                 | 描述                                           |
| ---- | ------------------------------------------ | ---------------------------------------------- |
| 1    | public static final int PUBLIC             | 0x00000001                                     |
| 2    | public static final int PRIVATE            | 0x00000002                                     |
| 3    | public static final int PROTECTED          | 0x00000004                                     |
| 4    | public static final int STATIC             | 0x00000008                                     |
| 5    | public static final int FINAL              | 0x00000010                                     |
| 6    | public static final int SYNCHRONIZED       | 0x00000020                                     |
| 7    | public static final int VOLATILE           | 0x00000040                                     |
| 8    | public static final int TRANSIENT          | 0x00000080                                     |
| 9    | public static final int NATIVE             | 0x00000100                                     |
| 10   | public static final int INTERFACE          | 0x00000200                                     |
| 11   | public static final int ABSTRACT           | 0x00000400                                     |
| 12   | public static final int STRICT             | 0x00000800                                     |
|      |                                            |                                                |
| 13   | public static String **toString**(int mod) | 返回描述指定修饰符中的访问修饰符标志的字符串。 |

### 3、java.lang.reflect.Constructor

| 序号 | 方法                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | public Annotation[] **getDeclaredAnnotations**()             | 返回构造器上的所有注解类型                                   |
| 2    | public <T extends Annotation> T **getAnnotation**(Class<T> annotationClass) | 返回构造器上指定的注解类型                                   |
| 3    | public int **getModifiers**()                                | 以整数形式返回此 Constructor 对象所表示构造方法的 Java 语言修饰符。应该使用 Modifier 类对这些修饰符进行解码。 |
| 4    | public String **getName**()                                  | 以字符串形式返回此构造方法的名称。它总是与构造方法的声明类的简单名称相同。 |
| 5    | public Class<?>[] **getParameterTypes**()                    | 按照声明顺序返回一组 Class 对象，这些对象表示此 Constructor 对象所表示构造方法的形参类型。 |
| 6    | public Class<?>[] **getExceptionTypes**()                    | 回一组表示声明throws的异常类型的 Class 对象                  |
|      |                                                              |                                                              |
| 7    | public T **newInstance**(Object... initargs)               throws InstantiationException,                      IllegalAccessException,                      IllegalArgumentException,                      InvocationTargetException | 使用此 Constructor 对象表示的构造方法来创建该构造方法的声明类的新实例，并用指定的初始化参数初始化该实例。 |
| 8    | public void **setAccessible**(boolean flag)                    throws SecurityException | 将此对象的 accessible 标志设置为指示的布尔值。值为 true 则指示反射的对象在使用时应该取消 Java 语言访问检查。值为 false 则指示反射的对象应该实施 Java 语言访问检查。 |



### 4、java.lang.reflect.Field

| 序号 | 方法                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | public Annotation[] **getDeclaredAnnotations**()             | 返回字段上的所有注解类型                                     |
| 2    | public <T extends Annotation> T **getAnnotation**(Class<T> annotationClass) | 返回字段上指定的注解类型                                     |
| 3    | public int **getModifiers**()                                | 以整数形式返回由此 Field 对象表示的字段的 Java 语言修饰符。应该使用 Modifier 类对这些修饰符进行解码。 |
| 4    | public Class<?> **getType**()                                | 返回一个 Class 对象，它标识了此 Field 对象所表示字段的声明类型。 |
| 5    | public String **getName**()                                  | 返回此 Field 对象表示的字段的名称。                          |
|      |                                                              |                                                              |
| 6    | public void **setAccessible**(boolean flag)                    throws SecurityException | 将此对象的 accessible 标志设置为指示的布尔值。值为 true 则指示反射的对象在使用时应该取消 Java 语言访问检查。值为 false 则指示反射的对象应该实施 Java 语言访问检查。 |
| 7    | public void **set**(Object obj,                 Object value)          throws IllegalArgumentException,                 IllegalAccessException | 将指定对象变量上此 Field 对象表示的字段设置为指定的新值。如果底层字段是静态字段，则忽略 obj 变量；它可能为 null。 |
| 8    | public Object **get**(Object obj)            throws IllegalArgumentException,                   IllegalAccessException | 返回指定对象上此 Field 表示的字段的值。如果底层字段是一个静态字段，则忽略 obj 变量；它可能为 null。 |



### 5、java.lang.reflect.Method

| 序号 | 方法                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | public Annotation[] **getDeclaredAnnotations**()             | 返回某方法上的所有注解类型                                   |
| 2    | public <T extends Annotation> T **getAnnotation**(Class<T> annotationClass) | 返回某方法上指定的注解类型                                   |
| 3    | public int **getModifiers**()                                | 以整数形式返回由此 Field 对象表示的字段的 Java 语言修饰符。应该使用 Modifier 类对这些修饰符进行解码。 |
| 4    | public Class<?> **getReturnType**()                          | 返回一个 Class 对象，该对象描述了此 Method 对象所表示的方法的正式返回类型。 |
| 5    | public String **getName**()                                  | 返回此 Field 对象表示的字段的名称。                          |
| 6    | public Class<?>[] **getParameterTypes**()                    | 按照声明顺序返回一组 Class 对象，这些对象表示此Method对象所表示方法的形参类型。 |
| 7    | public Class<?>[] **getExceptionTypes**()                    | 回一组表示声明throws的异常类型的 Class 对象                  |
|      |                                                              |                                                              |
| 8    | public void **setAccessible**(boolean flag)                    throws SecurityException | 将此对象的 accessible 标志设置为指示的布尔值。值为 true 则指示反射的对象在使用时应该取消 Java 语言访问检查。值为 false 则指示反射的对象应该实施 Java 语言访问检查。 |
| 9    | public Object **invoke**(Object obj,                      Object... args)               throws IllegalAccessException,                      IllegalArgumentException,                      InvocationTargetException | 对带有指定参数的指定对象调用由此 Method 对象表示的底层方法。对带有指定参数的指定对象调用由此 Method 对象表示的底层方法。 |



### 6、java.lang.reflect.Array

在java.lang.reflect包下还提供了一个Array类，Array对象可以代表所有的数组。程序可以通过使用Array类来动态的创建数组，操作数组元素等。

| 序号 | 方法                                                         | 描述                                       |
| ---- | ------------------------------------------------------------ | ------------------------------------------ |
| 1    | public static Object **newInstance**(Class<?> componentType,                                  int length)                           throws NegativeArraySizeException | 创建一个具有指定的组件类型和长度的新数组。 |
| 2    | public static void **set**(Object array,                        int index,                        Object value)                 throws IllegalArgumentException,                        ArrayIndexOutOfBoundsException | 将array数组中[index]元素的值修改为value。  |
| 3    | public static Object **get**(Object array,                          int index)                   throws IllegalArgumentException,                          ArrayIndexOutOfBoundsException | 返回指定数组对象中索引组件的值。           |

## 15.3 类加载器

- public static ClassLoader getSystemClassLoader()：返回系统类加载器。

- public static InputStream getSystemResourceAsStream(String name) ：从加载类的搜索路径中加载指定名称的资源。

- public ClassLoader getParent()：返回父加载器。  

- public InputStream getResourceAsStream(String name)：从加载类的搜索路径中加载指定名称的资源。 

- public Class<?> loadClass(String name)：指定类型的全名称加载字节码数据，并返回Class对象。 



