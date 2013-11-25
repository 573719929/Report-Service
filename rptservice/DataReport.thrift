namespace java com.baicdata.stat
include "ADP/Shared.thrift"
enum ORDER { ASC = 1, DESC = 2 }
struct queryOptions {
    1: string id,
    2: string startAt, # 20130801
    3: string endAt, # 20130809
    4: list <string> areaid=[], # 地域过滤，为空时则为全部
    5: Shared.FlowSrc source=0 # 流量来源过滤,为空时则为全部
}
struct pageOptions {
    1: i32 pageNumber = 1,
    2: i32 pageSize = 10,
    3: ORDER order = ORDER.ASC,
    4: string orderBy
}
struct Response {
    1: string id,
    2: i32 push,
    3: i32 show,
    4: i32 click,
    5: double cost,
    6: i32 bid,
    7: i32 bidres,
    8: double selfcost
}

struct reportResult {
    1: i32 totalSize, # 总的记录数
    2: i32 currentSize, # 当前结果的记录数
    3: i32 totalPage, # 总页数
    4: i32 pageNumber, # 当前页数
    5: list <Response> data # 结果的数组
}
service ReportService {
    /* 返回Adid的PushShowClickCost */
    reportResult AdReportByAdid(1: queryOptions q, 2: pageOptions p);
    /* 返回GroupId下所有广告的PushShowClickCost */
    reportResult AdReportByGroupId(1: queryOptions q, 2: pageOptions p);
    /* 返回PlanId下所有广告组的PushShowClickCost */
    reportResult GroupReportByPlanId(1: queryOptions q, 2: pageOptions p);
    /* 返回用户所有广告计划的ShowClickCost */
    reportResult PlanReportByUid(1: queryOptions q, 2: pageOptions p);
	
	/* 返回uid在startAt和endAt之间的所有消费,QueryOptions中的id是uid,areaid和source被忽略 */
	double getCostByUid(1: queryOptions q);
    
    /* 返回此Adid在各个地区的PushShowClickCost */
    reportResult AreaByAdid(1: queryOptions q, 2: pageOptions p);
    /* 返回此GroupId在各个地区的PushShowClickCost */
    reportResult AreaByGid(1: queryOptions q, 2: pageOptions p);
    /* 返回此PlanId在各个地区的PushShowClickCost */
    reportResult AreaByPid(1: queryOptions q, 2: pageOptions p);
    /* 返回此Uid的所有广告在各个地区的ShowClickCost */
    reportResult AreaByUid(1: queryOptions q, 2: pageOptions p);
    
    /* 返回此Adid在各个日期的PushShowClickCost */
    reportResult DayByAdid(1: queryOptions q, 2: pageOptions p);
    /* 返回此GroupId在各个日期的PushShowClickCost */
    reportResult DayByGid(1: queryOptions q, 2: pageOptions p);
    /* 返回此PlanId在各个日期的PushShowClickCost */
    reportResult DayByPid(1: queryOptions q, 2: pageOptions p);
    /* 返回此Uid的所有广告在各个日期的ShowClickCost */
    reportResult DayByUid(1: queryOptions q, 2: pageOptions p);
    
    /* 返回此Adid在各个来源的PushShowClickCost */
    reportResult SourceByAdid(1: queryOptions q, 2: pageOptions p);
    /* 返回此GroupId在各个来源的PushShowClickCost */
    reportResult SourceByGid(1: queryOptions q, 2: pageOptions p);
    /* 返回此PlanId在各个来源的PushShowClickCost */
    reportResult SourceByPid(1: queryOptions q, 2: pageOptions p);
    /* 返回此Uid的所有广告在各个来源的ShowClickCost */
    reportResult SourceByUid(1: queryOptions q, 2: pageOptions p);
    
    /* 返回此Adid在各个小时的PushShowClickCost */
    reportResult HourByAdid(1: queryOptions q, 2: pageOptions p);
    /* 返回此GroupId在各个小时的PushShowClickCost */
    reportResult HourByGid(1: queryOptions q, 2: pageOptions p);
    /* 返回此PlanId在各个小时的PushShowClickCost */
    reportResult HourByPid(1: queryOptions q, 2: pageOptions p);
    /* 返回此Uid的所有广告在各个小时的ShowClickCost */
    reportResult HourByUid(1: queryOptions q, 2: pageOptions p);
    
    /* 返回此Adid在各个Host的PushShowClickCost */
    reportResult HostByAdid(1: queryOptions q, 2: pageOptions p);
    /* 返回此GroupId在各个Host的PushShowClickCost */
    reportResult HostByGid(1: queryOptions q, 2: pageOptions p);
    /* 返回此PlanId在各个Host的PushShowClickCost */
    reportResult HostByPid(1: queryOptions q, 2: pageOptions p);
    /* 返回此Uid的所有广告在各个Host的ShowClickCost */
    reportResult HostByUid(1: queryOptions q, 2: pageOptions p);
    
    /* 返回此Adid在各个Adspace的PushShowClickCost */
    reportResult AdspaceByAdid(1: queryOptions q, 2: pageOptions p);
    /* 返回此GroupId在各个Adspace的PushShowClickCost */
    reportResult AdspaceByGid(1: queryOptions q, 2: pageOptions p);
    /* 返回此PlanId在各个Adspace的PushShowClickCost */
    reportResult AdspaceByPid(1: queryOptions q, 2: pageOptions p);
    /* 返回此Uid的所有广告在各个Adspace的ShowClickCost */
    reportResult AdspaceByUid(1: queryOptions q, 2: pageOptions p);
    
    /* nothing */
    void ping(1: i32 ignoreme)
}

