//=============================================================================
// This is an Arbiter for Read Transactions using Round Robin Algorithm for two Master
//=============================================================================

`timescale 1ns/1ns

module AXI_Arbiter_R (
    /********* System signals *********/
	input                       ACLK,
	input      	                ARESETn,
	/********** Master 0 **********/
    input                       m0_ARVALID,
    input                       m0_RREADY,
	/********** Master 1 **********/
    input                       m1_ARVALID,
    input                       m1_RREADY,
	/********** Slave **********/
    input                       s_RVALID,
    input                       s_RLAST,
	
    output reg                  m0_rgrnt,
	output reg	                m1_rgrnt
);

    // state define
    parameter AXI_MASTER_0 = 0;
    parameter AXI_MASTER_1 = 1;
    
    reg state, next_state;

    //---------------------------------------------------------
    always @(*) begin
        case (state)
            AXI_MASTER_0: begin                 // 0 --> 1
                if(m0_ARVALID)                  
                    next_state = AXI_MASTER_0;  
                else if(s_RVALID||m0_RREADY)    
                    next_state = AXI_MASTER_0;  
                else if(s_RLAST&&s_RVALID)      
                    next_state = AXI_MASTER_1;  
                else if(m1_ARVALID)             
                    next_state = AXI_MASTER_1;  
                else                            
                    next_state = AXI_MASTER_0;  
            end
            AXI_MASTER_1: begin                 // 1 --> 0
                if(m1_ARVALID)                  
                    next_state = AXI_MASTER_1;
                else if(s_RVALID||m1_RREADY)
                    next_state = AXI_MASTER_1;
                else if(s_RLAST&&s_RVALID)
                    next_state = AXI_MASTER_0;
                else if(m0_ARVALID)
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
    always @(*)begin
        case (state)
            AXI_MASTER_0: {m0_rgrnt,m1_rgrnt} = 2'b10;
            AXI_MASTER_1: {m0_rgrnt,m1_rgrnt} = 2'b01;
            default:      {m0_rgrnt,m1_rgrnt} = 2'b00;
        endcase
    end

endmodule