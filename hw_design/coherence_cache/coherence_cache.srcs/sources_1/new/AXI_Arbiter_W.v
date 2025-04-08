//=============================================================================
// This is an Arbiter for Write Transactions using Round Robin Algorithm for two Master
//=============================================================================

`timescale 1ns/1ns

module AXI_Arbiter_W (
    /********* System signals *********/
	input                       ACLK,
	input      	                ARESETn,
	/********** Master 0 **********/
    input                       m0_AWVALID,
    input                       m0_WVALID,
    input                       m0_BREADY,
	/********** Master 1 **********/
    input                       m1_AWVALID,
    input                       m1_WVALID,
    input                       m1_BREADY,
    /********** Slave **********/
    input                       s_AWREADY,
    input                       s_WREADY,
    input                       s_BVALID,
    
    output reg                  m0_wgrnt,
	output reg	                m1_wgrnt
);

    // state define
    parameter AXI_MASTER_0 = 0;
    parameter AXI_MASTER_1 = 1;
    
    reg state, next_state;

    //---------------------------------------------------------
    always @(*) begin
        case (state)
            AXI_MASTER_0: begin                 // 0 --> 1
                if(m0_AWVALID)                  
                    next_state = AXI_MASTER_0;  
                else if(m0_WVALID||s_WREADY)    
                    next_state = AXI_MASTER_0;  
                else if(s_BVALID&&m0_BREADY)    
                    next_state = AXI_MASTER_1;  
                else if(m1_AWVALID)             
                    next_state = AXI_MASTER_1; 
                else                            
                    next_state = AXI_MASTER_0;  
            end
            AXI_MASTER_1: begin                 // 1 --> 0
                if(m1_AWVALID)                  
                    next_state = AXI_MASTER_1;
                else if(m1_WVALID||s_WREADY)
                    next_state = AXI_MASTER_1;
                else if(s_BVALID&&m1_BREADY)
                    next_state = AXI_MASTER_0;
                else if(m0_AWVALID)
                    next_state = AXI_MASTER_0;
                else
                    next_state = AXI_MASTER_1;
            end
            default:
                next_state = AXI_MASTER_0;      
        endcase
    end


    //---------------------------------------------------------
    always @(posedge ACLK)begin
        if(!ARESETn)
            state <= AXI_MASTER_0;        
        else
            state <= next_state;
    end

    //---------------------------------------------------------
    always @(*) begin
        case (state)
            AXI_MASTER_0: {m0_wgrnt,m1_wgrnt} = 2'b10;
            AXI_MASTER_1: {m0_wgrnt,m1_wgrnt} = 2'b01;
            default:      {m0_wgrnt,m1_wgrnt} = 2'b00;
        endcase
    end

endmodule