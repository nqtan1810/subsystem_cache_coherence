`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// this is used to test snoop_controller
//////////////////////////////////////////////////////////////////////////////////


module snoop_controller_tb();

    reg clk, rst_n;
    
    // Snoop Response Channel
    // receive request from other Cache L1
    reg   s_ACVALID;
    wire s_ACREADY;
    // reg   [ADDR_WIDTH-1:0] s_ACADDR;
    reg   [1:0] s_ACSNOOP;
    // send response to other Cache L1
    wire s_CVALID;
    reg   s_CREADY;
    // output  [DATA_WIDTH-1:0] s_CDATA;
    wire s_CLAST;
    wire s_CHIT;
    
    // signals to control datapath
    // reg from checker_port2_REG
    reg   hit;
    wire state_tag_w_en;
    wire [3:0] control_offset;
    wire bus_in_reg_en;
    wire hit_miss_reg_en;

    initial begin
        clk = 0;
        rst_n = 0;
        s_ACVALID = 0;
        s_ACSNOOP = 0;
        s_CREADY  = 0;
        hit       = 0;
        #10;
        rst_n = 1;
        #100;
        repeat(1) @(posedge clk);
        s_ACVALID <= 1;
        s_ACSNOOP <= 1;
        s_CREADY  <= 1;
        hit       <= 1;
        
        repeat (1000) @(posedge clk);
        $finish;
    end
    
    initial begin
        forever #5 clk = ~clk;
    end
    
    snoop_controller dut0
(
    // system signals
    .ACLK(clk),
    .ARESETn(rst_n),
    
    // Snoop Response Channel
    // receive request from other Cache L1
    .s_ACVALID(s_ACVALID),
    .s_ACREADY(s_ACREADY),
    // input   [ADDR_WIDTH-1:0] s_ACADDR(),
    .s_ACSNOOP(s_ACSNOOP),
    // send response to other Cache L1
    .s_CVALID(s_CVALID),
    .s_CREADY(s_CREADY),
    // output  [DATA_WIDTH-1:0] s_CDATA(),
    .s_CLAST(s_CLAST),
    .s_CHIT(s_CHIT),
    
    // signals to control datapath
    // input from checker_port2_REG
    .hit(hit),
    .state_tag_w_en(state_tag_w_en),
    .control_offset(control_offset),
    .bus_in_reg_en(bus_in_reg_en),
    .hit_miss_reg_en(hit_miss_reg_en)
);

endmodule
