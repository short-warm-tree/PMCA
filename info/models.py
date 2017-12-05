from django.db import models


# Create your models here.
class Info(models.Model):
    COLLEGE_CHOICES = (

        ('1', '计算机学院'),
        ('2', '软件学院'),
        ('3', '电子信息学院'),
        ('4', '电气信息学院'),
        ('5', '数学学院'),
        ('6', '经济学院'),
        ('7', '空天科学与工程学院'),
        ('8', '高分子科学与工程学院'),
        ('9', '材料科学与工程学院'),
        ('10', '制造科学与工程学院'),
        ('11', '建筑与环境学院'),
        ('12', '水利水电学院'),
        ('13', '化学工程学院'),
        ('14', '轻纺与食品学院'),
        ('15', '法学院'),
        ('16', '艺术学院'),
        ('17', '文学与新闻学院'),
        ('18', '外国语学院'),
        ('19', '马克思主义学院（政治学院）'),
        ('20', '物理科学与技术学院（核科学与工程技术学院）'),
        ('21', '化学学院'),
        ('22', '生命科学学院'),
        ('23', '灾后重建与管理学院'),
        ('24', '公共管理学院'),
        ('25', '商学院'),
        ('26', '华西基础医学与法医学院'),
        ('27', '华西临床医学院'),
        ('28', '华西口腔医学院'),
        ('29', '华西公共卫生学院'),
        ('30', '华西药学院'),
        ('31', '吴玉章学院'),
        ('32', '体育学院'),
        ('33', '网络空间安全学院'),
        ('33', '研究生院'),
        ('34', '其他'),

    )
    SEX_CHOICES = (
        ('1', '男'),
        ('0', '女'),

    )

    name = models.CharField(max_length=5, default='', verbose_name='姓名')
    grade = models.CharField(max_length=5, default='', verbose_name='年级')
    stunum = models.CharField(max_length=13, default='', verbose_name='学号')
    college = models.CharField(max_length=2, default='27', choices=COLLEGE_CHOICES, verbose_name='学院')
    major = models.CharField(max_length=10, default='', verbose_name='专业')
    gender = models.CharField(max_length=1, default='1', choices=SEX_CHOICES, verbose_name='性别')

    skill = models.TextField(max_length=200, default='', verbose_name='技能')
    prove = models.TextField(max_length=255, default='', verbose_name='技能证明材料')
    done = models.TextField(max_length=500, default='', verbose_name='协会贡献')

    def __str__(self):
        return self.name
